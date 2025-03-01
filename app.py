from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')

if __name__ == '__main__':
    app.run(debug=True)
