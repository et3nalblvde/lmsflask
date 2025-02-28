from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        surname = request.form["surname"]
        name = request.form["name"]
        email = request.form["email"]
        education = request.form["education"]
        profession = request.form["profession"]
        gender = request.form["gender"]
        motivation = request.form["motivation"]
        stay = request.form["stay"]

        return f"<h2>Спасибо за вашу заявку, {name} {surname}!</h2>"

    professions = [
        "Инженер-исследователь", "Пилот", "Строитель", "Экзобиолог", "Врач", "Инженер по терраформированию",
        "Климатолог", "Специалист по радиационной защите", "Астрогеолог", "Гляциолог", "Инженер жизнеобеспечения",
        "Метеоролог", "Оператор марсохода", "Киберинженер", "Штурман", "Пилот дронов"
    ]

    return render_template("form.html", professions=professions)


if __name__ == "__main__":
    app.run(debug=True)
