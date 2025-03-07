from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Добавьте секретный ключ для использования flash-сообщений

# Пример данных для проверки
valid_astronauts = {
    "astro1": "password1",
    "astro2": "password2"
}

valid_captains = {
    "cap1": "token1",
    "cap2": "token2"
}

@app.route('/')
@app.route('/index/<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        astronaut_id = request.form.get('astronaut_id')
        astronaut_password = request.form.get('astronaut_password')
        captain_id = request.form.get('captain_id')
        captain_token = request.form.get('captain_token')

        if (astronaut_id in valid_astronauts and valid_astronauts[astronaut_id] == astronaut_password) and \
           (captain_id in valid_captains and valid_captains[captain_id] == captain_token):
            flash('Доступ разрешен', 'success')
            return redirect(url_for('index', title="Успешный доступ"))
        else:
            flash('Ошибка в данных. Попробуйте снова.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html', title="Аварийный доступ")

if __name__ == '__main__':
    app.run(debug=True)
