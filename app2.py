from flask import Flask, request, render_template
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import io
import bcrypt
import urllib2, urllib, random, string  
import pymongo
from pymongo import MongoClient
from pprint import pprint
import json
from validate_email import validate_email
      
app = Flask(__name__)
inventory = None
db = None
shoppingCart = {}



@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});


def renderTemplate(type):
  if type == "Login":
    print("Rendering login page template")
    return render_template("login.html")
  elif type == "Error":
    return render_template("error.html")

def validateCredentials(email,password):
  print("validateCredentials")
  #validates email by checking the DNS and if it has SMTP server using library functions
  is_valid = validate_email(email,verify=True)
  print "was it valid? ", is_valid
  if is_valid: 
    if userExists(email, password):
      print "user exists"
      return True
    else:
      return False
  else:
    return False

def getDBConnection():
  try:

    client = MongoClient('localhost', 27017)
    db = client.Inventory
    return db

  except Exception, e:
    print str(e)

def printUsers():
  collection = db.Users
  cursor = collection.find({})
  for document in cursor: 
    print(document)

def createUser(email, hashed_pwd):
  print("in create user")
  try:
    db.Users.insert_one(
      {
        "email": email,
        "password": hashed_pwd
      })

  except Exception, e:
    print str(e)

def userExists(email):
  try:
    items = db.Users.find({"email": email})
    if len(items) > 0:
      return True
    else:
      return False
  
  except Exception, e:
    print str(e)  

def retrieveUser(email):
  try:
    items = db.Users.find({"email": email})
    for item in items:
      print(item)
    
    return items
    
  except Exception, e:
    print str(e)  

def updateUser(email, hashed_pwd):
  try:
    db.Users.update(
      {"email": email},
      { 
        "$set":
          {
            "password": hashed_pwd
          }
      }
    )
    
  except Exception, e:
    print str(e)
  
def deleteUser(email):
  try:
    db.Users.remove({"email": email})
    
  except Exception, e:
    print str(e)

def hash_password(password):
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash_password

def getCredentials():
  email = raw_input("Please enter your email: ")
  password = raw_input("Please enter your password: ")
  return (email, password)

@app.route('/signUp', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return (user, password)

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

def addToCart(price, name, qty, pic=None, description=None): 
  shoppingCart.append(
      {
        "price": price,
        "name": name,
        "quantity": qty,
        "pic": pic,
        "description": description
      })

def removeFromCart(price, name, qty, pic=None, description=None): 
  for item in shoppingCart:
    if item["name"] == "name":
      shoppingCart.pop(item, None)

def updateItemQuantityInCar(name, qty): 
  for item in shoppingCart:
    if item["name"] == name:
      #shoppingCart.update(item["quantity"] = qty)
  

@app.route('/login',methods=['GET'])
def login():
  getCredentials()
  if validCredentials(email,password):
    return renderTemplate("Login")
  else:
    return renderTemplate("Error")     


if __name__ == "__main__":
  db = getDBConnection()
  email, password = getCredentials()
  hashed_pwd = hash_password(password)
  createUser(email, hashed_pwd)
  validateCredentials(email, hashed_pwd)
  printUsers()



  app.run(port=8000,debug=True)
