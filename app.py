######################################
#### Assignment 12 - Web Scraping ####
########### Initialize App ###########
######################################

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd

app = Flask(__name__)

###################################
##### Set-up Mongo Connection #####
###################################

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


###############################
######### APP Routes ##########
###############################

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

###################################
############ End Script ###########
###################################