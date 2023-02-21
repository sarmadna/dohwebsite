from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfjhwjheasdf038asfhasdf'

from doh import routes