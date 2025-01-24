from flask import render_template, request
from datetime import datetime

def home_route():
    return render_template("home.html", message="Привет!", current_year=datetime.now().year)  # Передаем текущий год сюда

def register_route():
    return render_template("register.html")

def profile_route():
    name = request.args.get('name')
    surname = request.args.get('surname')
    birthdate = request.args.get('birthdate')
    hobbies = request.args.get('hobbies')
    photo = request.args.get('photo')
    return render_template('profile.html', name=name, surname=surname, birthdate=birthdate, hobbies=hobbies, photo=photo)

def anya():
    return "Easter egg"
