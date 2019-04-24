from flask import Flask, render_template, redirect, request, url_for, abort
from flask_login import UserMixin, LoginManager, current_user, login_user, login_required, logout_user
from backend.login import BELIF
from backend.flaskstuff import skey, Access

# get the Flask app up and running
app = Flask(__name__)
app.secret_key = skey 

# binding the LoginManager to the app
login_manager = LoginManager()
login_manager.init_app(app)

# creating a dict of owner(s)
users = {Access.user: {'password': Access.pwrd}}


# creating the user class
class User(UserMixin):
    pass

# load from the database users
@login_manager.user_loader
def user_loader(un):
    if Access.user not in users:
        return
    user = User()
    user.id = Access.user
    return user

# matching from the login form name field to the database username field
@login_manager.request_loader
def request_loader(request):
    Access.user = request.form.get('name')
    if Access.user not in users:
        return
    user = User()
    user.id = Access.user
    user.is_authenticated = request.form['password'] == users[Access.user]['password']
    return user

# the start page
@app.route('/')
@app.route('/home')
@app.route('/login', methods=['GET','POST'])
def login():
    form = BELIF()
    if request.method == 'GET':
        return render_template('access.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            Access.user = request.form['name']
            user = User()
            user.id = Access.user
            login_user(user)
            return redirect(url_for('beos'))
    else:
        return abort(404, 'Invalid!!!')

# the secure portion of the website
@app.route('/beos')
@login_required
def beos():
    owner =  current_user.id
    return render_template('owner.html', owner = owner)


# logout process
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
