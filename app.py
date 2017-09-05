from PIL import Image
from flask import Flask, request, render_template
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import io
import urllib2 as urllib2 
import urllib 
import random
import string
import pymongo
from pymongo import MongoClient


import json
from PIL import Image
from urllib2 import urlopen
      
app = Flask(__name__)

def renderTemplate(type):
  if type == "Login":
    print("Rendering login page template")
    return render_template("login.html")


@app.route('/login',methods=['GET'])
def login():

  return renderTemplate("Login")

if __name__ == "__main__":
  app.run(port=8000,debug=True)
