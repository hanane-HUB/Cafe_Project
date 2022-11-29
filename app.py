from flask import Flask, render_template, url_for, request, redirect, jsonify
# from models.user import User
from Cafe_Project.user.utils import check_login, add_user, check_username
from menu_items.utils import get_menuitems

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    username = request.form['user_name']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    if check_username(username):
        add_user(username=username, fname=first_name, lname=last_name, phone=phone, email=email, password=password)
        return render_template('index.html', autorize=True)
    else:
        return render_template('signup.html', error=True)


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            if check_login(request.form['username'], request.form['password']):
                foods = list(get_menuitems('food'))
                drinks = list(get_menuitems('drink'))
                return render_template('index.html', autorize=True, foods=foods, drinks=drinks)
            else:
                return render_template('login.html', error=True)
                # todo: error

        else:
            # todo: cashier panel
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)


