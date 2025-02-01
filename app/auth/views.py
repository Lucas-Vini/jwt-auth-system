from flask import Blueprint, request
from app.auth.handler.signup import SignUpHandler

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods = ['POST'])
def signup():
	data = request.json
	SignUpHandler(data.get("username"), data.get("password"))
	return "signup"

@auth.route("/login")
def login():
	return "login"

@auth.route("/logout")
def logout():
	return "logout"