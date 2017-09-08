from flask import Flask, request, render_template
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import io
import urllib2, urllib, random, string  
import pymongo
from pymongo import MongoClient
from pprint import pprint
import json
      
app = Flask(__name__)
inventory = None
db = None

def renderTemplate(type):
  if type == "Login":
    print("Rendering login page template")
    return render_template("login.html")
  elif type == "Error":
    return render_template("error.html")

def validCredentials():
  
  return True

def getInventoryDBConnection():
  try:

    client = MongoClient('localhost', 27017)
    db = client.Inventory
    return db

  except Exception, e:
    print str(e)

# def getUsersDBConnection():
#   try:

#     client = MongoClient('localhost', 27017)
#     db = client.Users
#     return db

#   except Exception, e:
#     print str(e)

def createInventory(price, name, qty, pic=None, description=None):
  try:
    db.Inventory.insert_one(
      {
        "price": price,
        "name": name,
        "quantity": qty,
        "pic": pic,
        "description": description
      })

  except Exception, e:
    print str(e)

def printInventory():
  collection = db.Inventory
  cursor = collection.find({})
  for document in cursor: 
    print(document)

def retrieveInventory(name):
  try:
    items = db.Inventory.find({"name": name})
    for item in items:
      print(item)
    
    return items
    
  except Exception, e:
    print str(e)  

def updateInventory(price, name, qty, pic=None, description=None):
  try:
    db.Inventory.update(
      {"name": name},
      { 
        "$set":
          {
            "price": price,
            "name": name,
            "quantity": qty,
            "pic": pic,
            "description": description
          }
      }
    )
    
  except Exception, e:
    print str(e)
  
def deleteInventory(name):
  try:
    db.Inventory.remove({"name": name})
    
  except Exception, e:
    print str(e)

@app.route('/login',methods=['GET'])
def login():
  if validCredentials():
    return renderTemplate("Login")
  else:
    return renderTemplate("Error")     


if __name__ == "__main__":
  
  db = getInventoryDBConnection()
  db.Inventory.remove({})
  createInventory(20,"Apple",1)
  createInventory(22,"Orange",2)
  createInventory(24,"Banana",1)
  printInventory()

  
  updateInventory(25,"Banana",4)
  print("updated Banana")
  printInventory()

  deleteInventory("Apple")
  print("deleted Apple")
  printInventory()

  createInventory(28,"Strawberry",5)
  deleteInventory("Orange")
  print("deleted Orange, will now retrieve Strawberry")
  retrieveInventory("Strawberry")
  
  #printInventory()
  #app.run(port=8000,debug=True)
