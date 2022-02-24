from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
        self.ninjas = []

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append(cls(dojo))
            print (all_dojos)
        return all_dojos
    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id =%(id)s;"
        results = connectToMySQL("dojos_ninjas").query_db(query, data)
        return cls(results[0])
    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        new_dojo = connectToMySQL("dojos_ninjas").query_db(query, data)
        return new_dojo

    @classmethod
    def new_ninja(cls, data):
        query ="INSERT INTO dojos (name) VALUES (%(ninja_id)s);"
        return connectToMySQL('dojos_ninjas').query_db(query, data)

