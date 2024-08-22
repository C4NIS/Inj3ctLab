from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

# Página inicial (opcional)
@app.route('/')
def index():
    return jsonify({"message": "Inj3ctLab API is running"})

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
    if username == "admin" and password == "secret":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Rota para listar usuários
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()

    result = []
    for user in users:
        result.append({
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'created_at': user[3]
        })

    return jsonify(result)

# Rota para adicionar usuário
@app.route('/api/v1/users', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'User added successfully'}), 201

# Rota para obter usuário por ID
@app.route('/api/v1/users/<int:id>', methods=['GET'])
def get_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        result = {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'created_at': user[3]
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'User not found'}), 404

# Rota para atualizar usuário
@app.route('/api/v1/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    name = data.get('name')
    email = data.get('email')

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, id))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'User updated successfully'})

# Rota para deletar usuário
@app.route('/api/v1/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
