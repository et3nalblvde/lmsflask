from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)

@app.route('/distribution')
def distribution():
    astronauts = ["Иван Иванов", "Мария Петрова", "Сергей Сидоров", "Анна Кузнецова", "Дмитрий Павлов"]
    return render_template('distribution.html', astronauts=astronauts)

if __name__ == '__main__':
    app.run(debug=True)
