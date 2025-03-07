from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)

@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    if gender == 'male':
        wall_color = 'blue' if age > 21 else 'lightblue'
    elif gender == 'female':
        wall_color = 'red' if age > 21 else 'lightpink'
    else:
        wall_color = 'white'

    martian_img = 'adult_martian.png' if age > 21 else 'child_martian.png'

    return render_template('table.html', wall_color=wall_color, martian_img=martian_img)

if __name__ == '__main__':
    app.run(debug=True)
