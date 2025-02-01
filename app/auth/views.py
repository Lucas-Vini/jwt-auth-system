from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
	return "signup"

@auth.route("/login")
def login():
	return "login"

@auth.route("/logout")
def logout():
	return "logout"