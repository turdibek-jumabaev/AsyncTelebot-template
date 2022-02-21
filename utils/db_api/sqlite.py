import sqlite3

class Datebase:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db
    
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
    
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        data = None
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = connection.fecthone()
        if fetchall:
            data = connection.fetchall()
        connection.close()
        return data 
    
    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)
    
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    
    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)
    
    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)
    
    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    
    def count_users(self):
        sql = """
        select count(*) from Users;
        """
        return self.execute(sql=sql, fetchone=True)
    
    def update_user_email(self, email, id):

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        command = self.execute(sql, parameters=(email, id), commit=True)
        return command

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")