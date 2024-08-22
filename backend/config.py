# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_qualquer'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'seu_usuario_mysql'
    MYSQL_PASSWORD = 'sua_senha_mysql'
    MYSQL_DB = 'nome_do_banco_de_dados'
