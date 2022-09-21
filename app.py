from flask import Flask, render_template
from weatherapp import Hour,Weather

app = Flask(__name__)

@app.route('/')
def home():
#  return render_template("home.html")

@app.route("/Hour/<int:id>")
def Hour(id):
  #### Add template variables as 
  #### variable assignment arguments
#  return render_template("weatherapp.sql", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id])

#import mysql.connector
#establishing the connection
#conn = mysql.connector.connect(
#   user='root', password='password', host='127.0.0.1', database='mydb')

#from application import app

#if __name__ == "__main__":
#    app.run(debug=True, host='0.0.0.0')
