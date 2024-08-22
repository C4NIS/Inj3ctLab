from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    return "Inj3ctLab Backend is Running!"

if __name__ == '__main__':
    app.run(debug=True)
