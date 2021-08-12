from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/scrape")
def scraper():
    
    ## get a record from dict
    mars_info_dict = mongo.db.mars_info_dict
    ## call scrape function
    data = scrape_mars.scrape()
    ## update db
    mars_info_dict.update({}, data, upsert=True)
    ## return to "/" route
    return redirect("/")
    

@app.route("/")
def index():

    ## get a record from dict
    mars_info_dict = mongo.db.mars_info_dict.find_one()
    ## return template and data
    return render_template("index.html", mars_data_dict = mars_info_dict)
    
    
if __name__ == "__main__":
    app.run(debug=True)

