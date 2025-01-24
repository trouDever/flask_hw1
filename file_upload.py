from flask import request
import os

def save_file():
    uploaded_file = request.files.get("file")
    if uploaded_file:
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        return f"Файл {uploaded_file.filename} загружен."
    return "Ошибка"
