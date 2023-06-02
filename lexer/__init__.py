from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '9f5ac35a1742f4f096316546'


from lexer import routes