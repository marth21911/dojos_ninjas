from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja_model import Ninja 
from flask_app.models.dojo_model import Dojo

#======LETS MAKE A NINJA====================
@app.route ("/create_ninja")
def create_ninja_pg():
    dojos= Dojo.all_dojos()
    #^==========Goes to ===============================here
    return render_template("create_ninja.html", dojos = dojos)



@app.route("/createNinja", methods = ["POST"])
def create_ninja():
    data = {
        "first_name" : request.form ["fname"],
        "last_name" : request.form [ "lname"],
        "age" : request.form ["age"],
        "dojos_id" : request.form ["dojo"]
    }
    new_ninja = Ninja.createNinja(data)
    return redirect ("/")

# takes in the id through the href link, turns into data to dictionary
@app.route("/one_dojo/<dojo_id>")
def one_dojo(dojo_id):
    data = {
        "id" : dojo_id
    }
    dojo = Dojo.one_dojo(data)
    # ran a query to get the dojo name
    ninjas_n_dojo = Ninja.all_ninjas_in_dojo(data)
    # then took the same data and got my ninjas that go with it from classmethod
    return render_template("one_dojo.html", ninjas = ninjas_n_dojo, dojo = dojo )