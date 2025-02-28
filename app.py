from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def mission():
    return "Миссия Колонизация Марса"

@app.route('/index')
def motto():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br><br>Человечеству мала одна планета.<br><br>Мы сделаем обитаемыми безжизненные пока планеты.<br><br>И начнем с Марса!<br><br>Присоединяйся!"

@app.route('/image_mars')
def image_mars():
    html_content = """
    <!DOCTYPE html>
    <html lang='ru'>
    <head>
        <meta charset='UTF-8'>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src='https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg' alt='Изображение Марса' width='500'>
        <p>Вот он, загадочный красный Марс!</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
