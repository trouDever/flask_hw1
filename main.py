from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os
from file_upload import save_file  # Импортируем функцию для загрузки файла
from routes import home_route, register_route, profile_route, anya

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'your_secret_key'  #без него не робит и выдает ошибку для flask_wtf


def check_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age >= 18


@app.route('/')
def home():
    return home_route()


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        birthdate = datetime.strptime(request.form['birthdate'], "%Y-%m-%d")
        hobbies = request.form['hobbies']
        photo = request.files['photo']

        if len(name) < 2 or len(surname) < 2:
            error_message = "Введи настоящее имя"
            return render_template('register.html', error_message=error_message)

        if not check_age(birthdate):
            error_message = "Ты еще маленький"
            return render_template('register.html', error_message=error_message)

        if photo:
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
            photo.save(photo_path)

        return render_template('account.html', name=name, surname=surname, birthdate=birthdate, hobbies=hobbies, photo=photo.filename)

    return render_template('register.html')


@app.route("/upload", methods=["POST"])
def upload():
    return save_file()


@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Профиль пользователя
@app.route('/profile')
def profile():
    name = request.args.get('name')
    surname = request.args.get('surname')
    birthdate = request.args.get('birthdate')
    hobbies = request.args.get('hobbies')
    photo = request.args.get('photo')
    return render_template('account.html', name=name, surname=surname, birthdate=birthdate, hobbies=hobbies, photo=photo)

# Пасхалка
@app.route('/anya')  # Ваш "easter egg" маршрут
def easter_egg():
    return anya()

if __name__ == "__main__":
    app.run(debug=True)
