import os
import json
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)

@app.route('/member')
def member():
    with open('templates/crew.json', 'r', encoding='utf-8') as f:
        crew = json.load(f)
    random_member = random.choice(crew)
    return render_template('member.html', member=random_member)

if __name__ == '__main__':
    app.run(debug=True)
