from flask import Flask,render_template,request,redirect
from registration_db import JsonDB
app = Flask(__name__)
dbs = JsonDB()
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_registration",methods = ['post'])
def preform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    dob = request.form.get('user_dob')
    password = request.form.get('user_password')
    response = dbs.insert(name,email,dob,password)
    if response:
        return render_template("login.html",message = "Registration Done Succesfully")
    else:
        return render_template("login.html",message = "Email Already Exits")

@app.route("/perform_login",methods = ['post'])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbs.authenticate(email,password)

    if response:
        return redirect("/profile")
    else:
        return "Invalid Password"

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route('/NER')
def ner():
    return render_template("ner.html")

app.run(debug=True)