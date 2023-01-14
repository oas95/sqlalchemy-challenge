# Importing Dependencies 
import numpy as np 
import re
import datetime as dt

import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import creat_engine, func

from flask import Flask, jsonify 

# Database Setup

engine = creat_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model 
base = automap_base()

# Reflect the tables 
base.prepare(engine, reflect = True)

# Save references to the tables 

Measurement = base.classes.measurements 

Station = base.classes.station 

# Flask Setup

app = Flask(__name__)

# Flask Routes 

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter ass YYYY-MM-DD/YYYY-MM-DD"
    )

# Precipitation App Route  
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Creating session to database
    session = Session(engine)
    
    # Query Measument
    results = (session.query(Measurement.date, Measurement.tobs)
               .order_by(Measurment.date))
    
    #Creating a Dictonary for Precipitation Date
    precipitation_date_tobs = []
    for each_row in results:
        dt_dict = {}
        dt_dict["date"] = each_row.date
        dt_dict["tobs"] = each_row.tobs
        precipitation_date_tobs.append(dt_dict)

    return jsonify(precipitation_date_tobs)

# Stations App Route 

# Tobs App Route 

# Start App Route 

# Start/End App Route