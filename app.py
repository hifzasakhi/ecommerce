import os
import bcrypt
import pymongo
from pymongo import MongoClient
from flask import Flask,render_template, request,json
from validate_email import validate_email

app = Flask(__name__)
inventory = None
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

if __name__=="__main__":
  db = getDBConnection()
  app.run()
