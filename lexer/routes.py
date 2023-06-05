from lexer import app
from flask import render_template
from .forms import CodeForm, TreeForm
from .scripts.lexical import tokenize
from .scripts.tree import build_expression_tree

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
    if form.validate_on_submit():
        code = form.code.data
        tokens = tokenize(code)
        return render_template('output_lexer.html', form=form, tokens=tokens)
     
    return render_template('lexer.html', form=form, tokens=None)



@app.route('/tree', methods=['GET', 'POST'])
def tree():
    form = TreeForm()
    if form.validate_on_submit():
        expression=form.expression.data
        tree = build_expression_tree(expression)
        return render_template('tree.html', form=form, tree=tree, expression=expression)
    
    return render_template('tree.html', form=form, tree=None, expression=None)