from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
import time

app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY'] = '1e3a138e2853594f9489e60de470ed60'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page', command="Now shoo")

@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Me', text='')

@app.route("/places")
def places():
  return render_template('places.html', subtitle='Places I\'ve Been', text='Take a look at where I was this spring!')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Thanks {form.username.data}! This doesn\'t register you for anything, thanks anyways!', 'info')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")