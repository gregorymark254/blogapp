from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcdf1e982461e411b1d6627716bef3bf'

posts = [
    {
        'author': 'Gregory Mark',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Joseck Osugo ',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 29, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login successful for {form.email.data}!', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'Login unsuccessful for {form.email.data}!', 'danger')
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
