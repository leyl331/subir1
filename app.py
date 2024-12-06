




from flask import Flask, render_template
import random
import time
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grafico')
def grafico():
    return render_template('tabla.html')

if __name__ == '__main__':
    app.run(debug=True)
