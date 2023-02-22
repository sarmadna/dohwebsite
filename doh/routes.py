from doh import app
from flask import render_template

@app.route('/')
def main():
    return render_template('main.html', title='Main')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')