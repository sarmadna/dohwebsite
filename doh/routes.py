from doh import app
from flask import render_template

@app.route('/')
def main():
    return render_template('main.html', title='Main')

@app.route('/departments')
def departments():
    return render_template('departments.html', title='Departments')

@app.route('/directorates')
def directorates():
    return render_template('directorates.html', title='Directorates')

@app.route('/forms')
def forms():
    return render_template('forms.html', title='Forms')

@app.route('/registration')
def registration():
    return render_template('registration.html', title='Registration')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
