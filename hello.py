from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#bootstrap initialization
app = Flask(__name__)
bootstrap = Bootstrap(app)
#wtf-form config
app.config['SECRET_KEY'] = '960812'


class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')       



@app.route('/', methods=['GET','POST']) #register the view function as a handler for GET and POST requests. 
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', myform=form, name=name)

