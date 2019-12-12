from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime

class GetMale(Resource):
    
    connection = DbConfig()
    
    def get(self):
        update = "UPDATE Male SET state='Asignado' WHERE state IS NULL"
        self.connection.update(update)
        query = """SELECT ID_MALE, physicalConformation, state
                        FROM Male WHERE state = 'Asignado' OR state is NULL 
                        """
        males = [] 
        result = self.connection.read(query)
        for male in result:
            males.append({'id': male[0],'conformation': male[1], 'state': male[2]})
        
        return jsonify({'males': males})
        
class RemoveMale(Resource):
    connection = DbConfig()
    
    def put (self, id):
        query = """UPDATE Male SET state='{}' WHERE ID_MALE = {}""".format('Baja',id)
        return self.connection.update(query)

class ExamsMale(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        update = "UPDATE MaleExam SET examResult='Examen no reportado' WHERE examResult IS NULL"
        self.connection.update(update)
        query = """SELECT ID_EXAM, EXAM_DATE, examResult, ExamCat.examName AS name, ExamCat.examDescription AS description 
                    FROM MaleExam 
                    INNER JOIN ExamCat ON ID_EXAM_CAT = MaleExam.ID_EXAM"""
        exams = [] 
        result = self.connection.read(query)
        for exam in result:
            exams.append({'id': exam[0],'date': datetime.strftime(exam[1], '%d/%m/%Y'), 'result': exam[2],'name': exam[3], 'description': exam[4]})
        
        return jsonify({'exams': exams})
        
    def put(self):
        ID_MALE = request.get_json('ID_MALE')
        ID_EXAM = request.get_json('ID_EXAM')
        EXAM_DATE = request.get_json('EXAM_DATE')
        examResult = request.get_json('examResult')
        query = "UPDATE MaleExam SET examResult='{}' WHERE ID_MALE = {} AND ID_EXAM = {} AND EXAM_DATE = '{}'".format(examResult['examResult'], ID_MALE['ID_MALE'],ID_EXAM['ID_EXAM'], EXAM_DATE['EXAM_DATE'])
        return self.connection.update(query)