from flask_mysqldb import MySQL
from flask import jsonify
class DaoRace():
    
    _database= ""
    _declaracion = ""
    _cursor = ""

    def ConectionDb (self):
        connector = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="root", password="root", hostname="localhost", databasename="softpig")            
        return connector
    
    def getRaces(self):
        mysql = MySQL(self.ConectionDb())
        _cursor = mysql.connection.cursor()
        query = "SELECT * FROM examcat"
        _cursor.execute(query)
        data = _cursor.fetchall()
        mysql.connection.commit()
        _cursor.close()
        for exam in data:
            examcat = [
                {
                    "idExam": exam[0],
                    "examName": exam[1],
                    "examDescription": exam[2],
                }
            ]
        print( examcat)
        return jsonify(examcat)

a = DaoRace()
print(a.getRaces())

"""        /// <summary>
        /// Solicita al objeto BD que realice una consulta a la BD
        /// </summary>
        /// <param name="cedula"></param>
        /// <param name="role"></param>
        /// <param name="password"></param>
        /// <returns>Retorna un DTOUsuario</returns>
        public DTOUsuario BuscarUsuario(string cedula, string role, string password)
        {
            int idUsuario = 1;
            string nombre = "", apellido = "";

            try {
                ConectarBD();
                declaracion = "SELECT * FROM Usuario WHERE cedula = '" + cedula + "' AND rol = '" + role + "' AND password = MD5('" + password + "');";
                reader = database.Consultar(declaracion);
            
                if (reader.HasRows)
                {
                    if (reader.Read())
                    {
                        idUsuario = reader.GetBoolean(0) ? 1 : 0;
                        nombre = reader.GetString(2);
                        apellido = reader.GetString(3);
                        database.CerrarConexion();
                        return new DTOUsuario(idUsuario, cedula, nombre, apellido, role, password);
                    }
                }
            }catch (MySqlException ex){
                 MessageBox.Show(ex.ToString());
            }
            database.CerrarConexion();
            return null;
        }
"""