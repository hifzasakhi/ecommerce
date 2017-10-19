import os
import bcrypt
import pymongo
from pymongo import MongoClient
from flask import Flask,render_template, request,json
from validate_email import validate_email

app = Flask(__name__)
inventory = None
<<<<<<< HEAD
shoppingCart = {}

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    email =  request.form['email']
    password = request.form['password']

    hashed_pwd = hash_password(password)
    createUser(email, hashed_pwd)
    printUsers()

def hash_password(password):
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash_password




    # if validateEmail(email) == False:
    # 	signUp()
    # print "email was validated"
    # return json.dumps({'status':'OK','email':email,'pass':password})


    # 	return json.dumps({'status':'OK','email':email,'pass':password})
    # if validateEmail(email):
    # 	print "email was valid"
    # 	return json.dumps({'status':'OK','email':email,'pass':password})
    # else:
    # 	print "email was NOT valid"
    # 	return json.dumps({'status':'ERROR'})

def validateEmail(email):
  print("validating email:")
  #validates email by checking the DNS and if it has SMTP server using library functions
  is_valid = validate_email(email,verify=True)
  print("finished validating email:")
  print "is_valid", is_valid
  return is_valid

=======
db = None
shoppingCart = {}


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
  if is_valid:o
    if userExists(email, password):
      print "user exists"
      return True
    else:
      return False
  else:
    return False
>>>>>>> 604f8ac2cd0448f622ae79b9d056d9ee32bffc35

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

<<<<<<< HEAD
if __name__=="__main__":
=======
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
      shoppingCart.update(item["quantity"] = qty)
  

@app.route('/login',methods=['GET'])
def login():
  getCredentials()
  if validCredentials(email,password):
    return renderTemplate("Login")
  else:
    return renderTemplate("Error")     


if __name__ == "__main__":
  
>>>>>>> 604f8ac2cd0448f622ae79b9d056d9ee32bffc35
  db = getDBConnection()
  app.run()
