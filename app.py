from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    user_data = {
        "title": "Анкета участника миссии",
        "surname": request.args.get('surname', 'Иванов'),
        "name": request.args.get('name', 'Иван'),
        "education": request.args.get('education', 'высшее'),
        "profession": request.args.get('profession', 'инженер'),
        "sex": request.args.get('sex', 'мужской'),
        "motivation": request.args.get('motivation', 'Исследовать новые миры!'),
        "ready": request.args.get('ready', 'True')
    }
    return render_template('auto_answer.html', **user_data)

if __name__ == '__main__':
    app.run(debug=True)
