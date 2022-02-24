from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo_model
class Ninja:
    def __init__(self, data):
        self.id = data ["id"]
        self.first_name = data ["first_name"]
        self.last_name = data ["last_name"]
        self.last_name = data["age"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]
        self.dojos_id = data ["dojos_id"]
#============Making some ninjas down heeeeeeereeeeee
    @classmethod
    def createNinja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);"
        return connectToMySQL('dojos_ninjas').query_db(query,data)

#===========Who parties where? Ninjas in their respective dojos, in a professional manner. 
    @classmethod
    def all_ninjas_in_dojo(cls, data):
        query = "Select * from ninjas join dojos ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s ;"
        #===query for joining dojos/ninjas using dojo id to specify
        results = connectToMySQL("dojos_ninjas").query_db(query, data)
        ninjas_in_dojo = []
        for row in results:
            #^starts looping information to be parsed
            one_ninja = cls(row)
            #^puts ninja info into list
            dojo_data = {
                #processes dojo info from JOIN
                "id" :row["dojos.id"],
                "name" : row["name"],
                "created_at" : row ["dojos.created_at"],
                "updated_at" : row ["dojos.updated_at"]
            }
            one_ninja.dojo = dojo_model.Dojo(dojo_data)
            #collects data==========^brings in the other class through the model.className
            ninjas_in_dojo.append(one_ninja)
            #puts all the data together in one instance
        return ninjas_in_dojo