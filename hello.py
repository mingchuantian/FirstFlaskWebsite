import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#for database setting
basedir = os.path.abspath(os.path.dirname(_file_))
#bootstrap initialization
app = Flask(__name__)
bootstrap = Bootstrap(app)
#wtf-form config
app.config['SECRET_KEY'] = '960812'
#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#database use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize database object
db = SQLAlchemy(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')       



@app.route('/', methods=['GET','POST']) #register the view function as a handler for GET and POST requests. 
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            #compare the dictionary value with new valur get from the form.
            flash('looks like you have changed your name!')
        session['name'] = form.name.data #This name now is saved into dictionary even the page is refreshed
        return redirect(url_for('index'))
    return render_template('index.html', myform=form, name=session.get('name'))

@app.route('/user/<username>')
def show_user(username):
    return 'User' + username


####### Database ########
#Define Role Model
class Role(db.Model):
    #Define table's name, otherwise assigned automatically
    __tablename__ = 'roles'
    #attributes of the model
    id = db.Column(db.Integer, primary_key=True)  #type and special config
    name = db.Column(db.String(64), unique=True)
    #__repr__ not necessary but can give string representation for testing
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username




#if __name__ == '__main__':
#    app.run(debug=True)
