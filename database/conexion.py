import pymysql

class Conexion:
    def __init__(self):
        self.Conexion = pymysql.connect( host='sql5.freesqldatabase.com', 
        user= 'sql5435107', passwd='f1mvje3Vx8', db='sql5435107' )
        self.cursor = self.Conexion.cursor()
    
    def cerrar_conexion(self):
        self.Conexion.close()
    
    def ejecutar_SQL(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def numberResult(self, sql):
        number = self.cursor.execute(sql)
        return number

