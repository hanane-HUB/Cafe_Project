from flask import Flask, render_template, url_for, request, redirect, abort
from core.db_manager import session
from receipt.utils import add_receipt, get_receipt, total_amount, check_user_receipt, update_total_amount, \
    get_filter_receipt
from tables.utils import check_table, reserve, get_filter_table
from user.utils import check_login, add_user, check_username, get_id
from menu_items.utils import get_menuitems, get_item, add_item
from order.utils import get_order_list, change_status, add_order, order_info

app = Flask(__name__)
global user_id, receipt_id


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
        global user_id
        user_id = get_id(username)
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
                global user_id
                user_id = get_id(request.form['username'])
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
    order_id = int(request.form["order_id"])
    change_status(order_id)
    orders_list = get_order_list()
    return render_template('orders_table.html', orders_list=orders_list)


@app.route('/add_new_order/<item_id>/<number>/<time_stamp>', methods=['POST', 'GET'])
def add_new_order(item_id, number, time_stamp):
    add_order(item_id=item_id, receipt_id=receipt_id, number=number, status='new order', time_stamp=time_stamp)
    foods = list(get_menuitems('food'))
    drinks = list(get_menuitems('drink'))
    return render_template('index.html', autorize=True, foods=foods, drinks=drinks)


@app.route('/MenuItem', methods=['GET', 'POST'])
def edit_menu_item():
    items = list(get_item())
    return render_template('menu_item.html', items=items)


@app.route('/create_item', methods=['GET', 'POST'])
def create_item():
    pass


@app.route('/create_receipt', methods=['GET', 'POST'])
def create_receipt():
    global receipt_id
    receipt_id = check_user_receipt(user_id)
    item_id = int(request.form["item_id"])
    if receipt_id:
        return redirect(url_for('add_new_order', item_id=item_id, number=1, time_stamp='12'))
        # todo: change number and time stamp
    else:
        table_id = check_table()
        if table_id:
            add_receipt(table_id, user_id, 0, False)
            receipt_id = check_user_receipt(user_id)
            reserve(table_id)
            return redirect(url_for('add_new_order', item_id=item_id, number=1, time_stamp='12'))
        else:
            abort(401)  # todo: app.errorhandler(404)-->render_template(''),404


@app.route('/display_receipt', methods=['GET', 'POST'])
def display_receipt():
    receipt = get_filter_receipt(receipt_id)
    table_id = receipt.table_id
    orders_info = order_info(receipt_id)
    update_total_amount(receipt_id)
    return render_template('receipt.html', user_id=user_id, receipt=receipt, table_id=table_id,
                           orders_info=orders_info, total=receipt.total_price)


@app.route('/user_receipt', methods=['GET', 'POST'])
def user_receipt():
    global receipt_id
    receipt_id = check_user_receipt(user_id)
    if receipt_id:
        return redirect(url_for('display_receipt'))
    else:
        abort(401)  # todo: app.errorhandler(404)-->render_template(''),404 | there's no order to have receipt


@app.route('/pay_receipt', methods=['GET', 'POST'])
def pay_receipt():
    receipt = get_filter_receipt(receipt_id)
    receipt.pay = True
    table = get_filter_table(receipt.table_id)
    table.available = True
    session.commit()
    return redirect(url_for('display_receipt'))


@app.route('/receipt_list', methods=['GET', 'POST'])
def receipt_list():
    receipts = get_receipt()
    for receipt in receipts:
        update_total_amount(receipt.id)
    return render_template('receipt_list.html', receipts=receipts)


@app.route('/paid_receipt', methods=['GET', 'POST'])
def paid_receipt():
    receipts = []
    for receipt in get_receipt():
        update_total_amount(receipt.id)
        if receipt.pay:
            receipts.append(receipt)
    return render_template('receipt_list.html', receipts=receipts)


if __name__ == '__main__':
    app.run(debug=True)
