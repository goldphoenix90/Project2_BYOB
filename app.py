import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/beer.sqlite"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
samples = Base.classes.beer


@app.route("/landing")
def landing():
    return render_template("landing.html")


@app.route("/")
def index():
    return render_template("index.html")

# enter zipcode, search should take you to the leaflet page with marker on map

@app.route("/abv")
def abv():
    return render_template("abv.html")   

#scatterplot
    # x= categories
    # y= abv
    # bubbles will be the beer name

@app.route("/brewmap")
def brewmap():
    return render_template("brewmap.html")

# connected to index page

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/sampleinfo")
def sampleInfo():
# Use Pandas to perform the sql query
    stmt = db.session.query(samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    
    data = {
        # donut will use beer category totals 
        "category_labels": df.categories.tolist(),
        "category_totals": df.groupby(["categories"])['name'].nunique().tolist(),
        "beer_name":df.name.tolist(),
        "abv": df.abv.tolist(),
        "zip_code": df.code.tolist(),
        "latitude": df.latitude.tolist(),
        "longitude": df.longitude.tolist(),
        "brewery_name": df.brewery_name.tolist(),
        }
    #data = df.groupby(["categories"])['name'].nunique().tolist()
    return jsonify(data)

    # print(df)
    # return jsonify(stmt)

@app.route("/mapinfo")
def mapInfo():
# Use Pandas to perform the sql query
    # id,brewery_id,name,categories,style,abv,beer_description,brewery_name,address1,city,state,code,country,latitude,longitude
    results = db.session.query(samples.name, samples.categories, samples.style, samples.abv, samples.brewery_name, samples.code, samples.latitude, samples.longitude).all()
    # data = json.load(open(in_file))
    data = []
    for result in results:
        res_dict = {}
        res_dict["beer_name"] = result[0]
        res_dict["category_labels"] = result[1]
        res_dict["style"] = result[2]
        res_dict["abv"] = result[3]
        res_dict["brewery_name"] = result[4]
        res_dict["zip_code"] = result[5]
        res_dict["latitude"] = result[6]
        res_dict["longitude"] = result[7]
        data.append(res_dict)

    geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["longitude"], d["latitude"]],
            },
        "properties" : d,
     } for d in data]
}
    

    print(geojson)

    #data = df.groupby(["categories"])['name'].nunique().tolist()
    # return jsonify(geojson)


#print("TYPE++++", type(geojson))

    #data = df.groupby(["categories"])['name'].nunique().tolist()
    # return render_template("brew-map.html", data=data)

@app.route("/beerinfo")
def beerInfo():
# Use Pandas to perform the sql query
   # id,brewery_id,name,categories,style,abv,beer_description,brewery_name,address1,city,state,code,country,latitude,longitude
   results = db.session.query(samples.name, samples.categories, samples.style, samples.abv, samples.brewery_name, samples.code, samples.latitude, samples.longitude).all()
   # data = json.load(open(in_file))
   data = []
   for result in results:
       res_dict = {}
       res_dict["beer_name"] = result[0]
       res_dict["category_labels"] = result[1]
       res_dict["style"] = result[2]
       res_dict["abv"] = result[3]
       res_dict["brewery_name"] = result[4]
    #    res_dict["zipcode"]=result[5]
     
      
       data.append(res_dict)
   print(data)
   #data = df.groupby(["categories"])['name'].nunique().tolist()
   return jsonify(data)

@app.route("/metadata/mapinfo")
def metaInfo():
  
    # id,brewery_id,name,categories,style,abv,beer_description,brewery_name,address1,city,state,code,country,latitude,longitude
    results = db.session.query(samples.name, samples.categories, samples.style, samples.abv, samples.brewery_name, samples.code, samples.latitude, samples.longitude).all()
    # data = json.load(open(in_file))
    data = []
    for result in results:
        res_dict = {}
        res_dict["beer_name"] = result[0]
        res_dict["category_labels"] = result[1]
        res_dict["style"] = result[2]
        res_dict["abv"] = result[3]
        res_dict["brewery_name"] = result[4]
        res_dict["zip_code"] = result[5]
        res_dict["lat"] = result[6]
        res_dict["long"] = result[7]
        data.append(res_dict)
    
    geojson = {
        "type": "FeatureCollection",
        "features": [
        {
            "type": "Feature",
            "geometry" : {
                "type": "Point",
                "coordinates": [d["long"], d["lat"]],
            },
            "properties" : d,
        } for d in data]
    }
    return jsonify(geojson)




@app.route("/brewguide")
def brewguide():
    return render_template("brewguide.html")


@app.route("/about")
def about():
    return render_template("about.html")


    
if __name__ == "__main__":
    app.debug=True
    app.run()

