from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/lexer')
def lexer():
    return render_template('lexer.html')


@app.route('/tree')
def tree():
    return render_template('tree.html')

if __name__ == '__main__':
    app.run()
