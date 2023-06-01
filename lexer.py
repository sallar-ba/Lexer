from flask import Flask, render_template
from forms import CodeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9f5ac35a1742f4f096316546'

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/lexer', methods=['GET', 'POST'])
def lexer():
    form = CodeForm()
    #if form.validate_on_submit():
        #code = form.Code.data
        # Function Call For Lexical and Syntax Analyzer
     
    return render_template('lexer.html', form=form)


@app.route('/tree')
def tree():
    return render_template('tree.html')

if __name__ == '__main__':
    app.run()
