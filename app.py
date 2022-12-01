from flask import Flask, render_template, url_for, request, redirect
from core.db_manager import session
from models.menu_items import MenuItems
from user.utils import check_login, add_user, check_username
from menu_items.utils import get_menuitems
from order.utils import get_order_list,change_status, add_order

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
        foods = list(get_menuitems('food'))
        drinks = list(get_menuitems('drink'))
        return render_template('index.html', autorize=True, foods=foods, drinks=drinks)
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


        else:
            foods = list(get_menuitems('food'))
            drinks = list(get_menuitems('drink'))
            return render_template('index.html', autorize='admin', foods=foods, drinks=drinks)

    return render_template('login.html', error=error)


@app.route('/orders')
def orders():
    orders_list = get_order_list()
    return render_template('orders_table.html', orders_list=orders_list)


@app.route('/orders', methods=['POST'])
def get_status_order():
    order_id = request.form["order_id"]
    order_id = int(order_id)
    change_status(order_id)
    orders_list = get_order_list()
    return render_template('orders_table.html', orders_list=orders_list)


@app.route('/home', methods=['POST'])
def add_new_order():
    item_id = request.form["item_id"]
    print(item_id)
    item_id = int(item_id)
    item = session.query(MenuItems).filter(MenuItems.id == item_id)
    item_id2 = 0
    for i in item:
        item_id2 = i.id
    add_order(item_id2, 1, 1, 'new order', '12')
    foods = list(get_menuitems('food'))
    drinks = list(get_menuitems('drink'))
    return render_template('index.html', autorize=True, foods=foods, drinks=drinks)


if __name__ == '__main__':
    app.run(debug=True)


