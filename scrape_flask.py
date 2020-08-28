from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrape_mars
from pymongo import MongoClient
import pymongo

# Create an instance of Flask

app = Flask(__name__, template_folder='template')
#app = Flask(__name__)


# app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# conn = "mongodb://localhost:27017/mission_to_mars"

# client = pymongo.MongoClient(conn)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
   
    mars = mongo.db.mars.find_one()
    
    # Return template and data
    return render_template("index.html", mars = mars)

# Route that will trigger the scrape function    
@app.route("/scrape")
def scrape():
    mars = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars, upsert=True)
    return redirect("/", code=302)

    

# # Given Already
if __name__ == "__main__":
    app.run(debug=True)
