from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choice.html', planet_name=planet_name)

if __name__ == '__main__':
    app.run(debug=True)
