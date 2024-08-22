from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# API para SQL Injection
@app.route('/api/v1/sqli', methods=['POST'])
def sqli():
    data = request.json
    query = data.get('query')
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        mysql.connection.commit()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()

# Endpoint de inserção de dados
@app.route('/api/v1/insert', methods=['POST'])
def insert_data():
    data = request.json
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(query, values)
        mysql.connection.commit()
        return jsonify({'message': 'Data inserted successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        cursor.close()

# Endpoint de login (opcional)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Autenticação simples para fins de exemplo
    if username == "admin" and password == "secret":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
