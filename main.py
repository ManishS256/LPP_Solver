from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify, send_file
from flask_restful import Resource, Api, reqparse
from werkzeug.exceptions import HTTPException
import json
import os

from iterator import *
from convert import *
from solve import *
from api import SolvetypeAPI, SolvefileAPI


app=None
api=None
app =Flask(__name__,template_folder='templates',static_folder='static')
api=Api(app)
app.app_context().push()

@app.route("/",methods=["GET"])
def homepage():
  if request.method=="GET":
    return render_template("index.html")

api.add_resource(SolvetypeAPI,"/api/solve/type")
api.add_resource(SolvefileAPI,"/api/solve/file")

if __name__ =="__main__":
  app.debug=True
  app.run(host='0.0.0.0',port='5000')