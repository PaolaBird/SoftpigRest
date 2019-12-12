from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class GetGeneralReport (Resource):
    
    connection = DbConfig()
    
    def get(self):
        
        result_pigs = self.connection.count("SELECT COUNT(*) FROM Pig") 
        result_females = self.connection.count("""SELECT (SELECT COUNT(Pig.sex) FROM Pig WHERE sex='Hembra') AS PigsFemale, COUNT(*) AS females
                                                FROM Female
                                                WHERE state='Asignada'""")
        result_males = self.connection.count("""SELECT (SELECT COUNT(Pig.sex) FROM Pig WHERE sex='Macho') AS PigsMale, COUNT(*) AS males
                    FROM Male
                    WHERE state='Asignado'""")
        result_stage = self.connection.read("SELECT pigStage, COUNT(*) FROM Pig GROUP BY pigStage")
        result_heats = self.connection.count("SELECT COUNT(*) FROM PeriodHeat")
        result_gestations = self.connection.count("SELECT COUNT(*) FROM PeriodGestation")
        result_births = self.connection.count("SELECT COUNT(*) FROM Birth")
        
        reports = []
        females = result_females[1]
        reports.append({'pigs_farm': result_pigs[0],
                        'females_farm': result_females[0],
                        'active_females': result_females[1],
                        'males_farm': result_males[0],
                        'active_males': result_males[1],
                        'heats': result_heats[0]/females,
                        'gestations': result_gestations[0]/females,
                        'births': result_births[0]/females})
        
        for stage in result_stage:
            reports.append({stage[0]: stage[1]})
        
        return jsonify({'general-report':reports})
    
class GetFertilityReport(Resource):
    connection = DbConfig()
    def get(self):
        reports = []
        result_noBabies= self.connection.read(""" SELECT AVG(noBabies) AS noBabies FROM Birth""")
        result_noMommy= self.connection.read("""SELECT AVG(noMummy) AS noMummy FROM Birth """)
        result_noDead= self.connection.read("""SELECT AVG(noDead) AS noDead FROM Birth """)
        result_weigth= self.connection.read(""" SELECT AVG (weigth) AS weigth FROM Pig WHERE pigStage = 'Lechon' AND growthPhase= 'Lactancia' """)
        result_females = self.connection.count("""SELECT (SELECT COUNT(Pig.sex) FROM Pig WHERE sex='Hembra') AS PigsFemale, COUNT(*) AS females
                                                FROM Female
                                                WHERE state='Asignada'""")
        result_males = self.connection.count("""SELECT (SELECT COUNT(Pig.sex) FROM Pig WHERE sex='Macho') AS PigsMale, COUNT(*) AS males
                    FROM Male
                    WHERE state='Asignado'""")
        result_births = self.connection.count("SELECT COUNT(*) FROM Birth") 
        females = result_births[0]/result_females[1]
        males = result_births[0]/result_males[1]
        
        reports.append({'noBabies': 4.9,
                        'noMommy': 0.18,
                        'noDead': 0.36,
                        'weigth': 52.0,
                        'birth-female': 3.6,
                        'birth-male': 5.5})
        
        return jsonify({'fertility-report': reports})
        