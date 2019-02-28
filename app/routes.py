from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username' : 'Harsha'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'Beautiful Day in Portland!'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers are so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

