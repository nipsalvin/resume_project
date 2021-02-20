from flask import Flask

app =  Flask(__name__)


@app.route('/')
def Home():
    return 'We are setting up, this should be the home page'

@app.route('/Services/')
def Services():
    return 'What we can do for you'

@app.route('/AboutUs/')
def AboutUs():
    return 'Just Incase you need to reach out'