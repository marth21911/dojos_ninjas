from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo

@app.route("/")
def dojo_home():
    dojos= Dojo.all_dojos()
    #^==========Goes to ===============================here
    return render_template("all_dojos.html", dojos = dojos)
#=============================================^^To html
@app.route("/create_dojo", methods = ["POST"])
def create_dojo():
    data = {
        "name" : request.form ["dojo_name"]
    }
    dojo_id = Dojo.new_dojo(data)
    return redirect ("/")


