
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from functools import wraps


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///myinvent.db")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# get date
current = datetime.now()
currentdate = current.strftime("%d-%m-%y")

# REGISTER/LOGIN/LOGOUT FUNCTIONS 
# Register function
@app.route("/register", methods=["GET", "POST"])
def register():
    # if request is POST
    if request.method == "POST":
        # get form elements
        name = request.form.get('name')
        email = request.form.get("email")
        password = request.form.get("password")
        repeat = request.form.get("pass-repeat")
        # all possible Condition checks
        if not name:
            flash('Name require')
            return render_template('register.html')
        if not email:
            flash("Email required")
            return render_template("register.html")

        if not password:
            flash("Password required")
            return render_template("register.html")

        if password != repeat:
            flash("Confirm Password must be the same")
            return render_template("register.html")
        # mail check
        emailcheck = db.execute("SELECT * FROM credentials WHERE email = ? ;",email)
        if len(emailcheck) > 0:
            flash("Email already exist \n Try SignIn ")
            return render_template("register.html")
        # Password hash "sha256"
        hash_pwd = generate_password_hash(password,"sha256")
        # update database
        register = db.execute("INSERT INTO credentials(name,email,hashed_pwd) VALUES(?,?,?);",name, email, hash_pwd)
        getid = db.execute("SELECT rowid FROM credentials WHERE email = ?", email)
        session["user_id"] = getid[0]['rowid']
        flash("Registered")
        return redirect(url_for("dashboard"))
    else:
        return render_template("register.html")

# login function
@app.route("/login", methods=["GET", "POST"])
def login():
    # clear current session
    session.clear()

    if request.method == "POST":
        # get form values
        email = request.form.get("email")
        password = request.form.get("password")
        # Check conditions
        if not email:
            flash("An Email is required ")
            return redirect("/login")
        if not password:
            flash("A Password is required ")
            return redirect("/login")
        rows = db.execute("SELECT * FROM credentials WHERE email = ?;",email)
        if not rows:
            flash("User not found, Register your email")
            return redirect("/register")
        # check if passwords match 
        if not check_password_hash(rows[0]["hashed_pwd"], password):
            flash("Password Doesn't match")
            return redirect("/login")
        session["user_id"] = rows[0]["rowid"]
        return redirect(url_for('dashboard'))
    else:
        return render_template("login.html")

# Logout function
@app.route("/logout", methods = ["GET","POST"])
@login_required
def logout():
    # clear all sessions  
    session.clear()
    return redirect("/login")

# displays dashboard 
@app.route("/dashboard", methods = ["GET","POST"])
@login_required
def dashboard():
        # get user info to be displayed 
        data = db.execute('SELECT name,email,rowid FROM credentials WHERE rowid = ?;', session['user_id'])
        zero = 0
        # remove products from inventory
        db.execute("DELETE FROM products WHERE rowid = ? AND qty = ?;",session["user_id"], zero)
        # get total products, total sales and total profit/loss data
        total_product = db.execute('SELECT Count(*) AS totalproducts FROM products WHERE rowid = ? AND qty > ?;', session['user_id'], zero)
        total_sales = db.execute('SELECT Count(*) AS totalsales FROM sales WHERE rowid = ?;', session['user_id'])
        total_pnl = db.execute('SELECT SUM(pnl) AS totalpnl FROM sales WHERE rowid = ?;', session['user_id'])
        return render_template("dashboard.html", data = data, total = total_product, total_sales=total_sales, total_pnl=total_pnl)

#home page function
@app.route("/", methods = ["GET","POST"])
@login_required
def home():
    # redirect to dashboard 
    if session['user_id']:
        return redirect(url_for('dashboard'))
    else:
        return  redirect(url_for('login'))

# add product function
@app.route("/addproducts", methods = ["GET","POST"])
@login_required
def addproduct():
    # get input data
    if request.method == "POST":
        name = request.form.get("productname")
        qty = request.form.get("quantity")
        price = request.form.get("price")
        # add data to invertory
        db.execute("INSERT INTO products(rowid,name,qty,price) VALUES(?,?,?,?);",session["user_id"], name, qty, price)
        flash("Product Added")
        return redirect(url_for("dashboard"))

# create_invoice
@app.route("/create_invoice", methods = ["GET","POST"])
@login_required
def create_invoice():
    # get invoice data
    if request.method == "POST":
        name = request.form.get('customer_name')
        qty = request.form.get('in_quantity')
        price = request.form.get('in_price')
        date = currentdate
        product = request.form.get('products')
        row = db.execute("SELECT qty FROM products WHERE rowid = ? AND name = ?;",session["user_id"], product)
        qty1 =row[0]['qty']
        qty = int(qty)
        # check if product is available
        if qty1 < 0:
            db.execute("DELETE FROM products WHERE rowid = ? AND name = ?;",session["user_id"], product)
            flash("Not Found")
            return redirect(url_for("dashboard"))
        #check for product in inventory 
        if qty > qty1:
            flash("Out of inventory range")
            return redirect(url_for("dashboard"))
        # get the remaining Quantity
        remainder = (qty1 - qty)
        row_price = db.execute("SELECT price FROM products WHERE rowid = ? AND name = ?;",session["user_id"], product)
        price = int(price)
        row_price = row_price[0]['price']
        # get the pnl
        pnl = qty * (price - row_price)
        # add data to sales db
        db.execute("INSERT INTO sales(rowid,name,qty,price,date,product,pnl) VALUES(?,?,?,?,?,?,?);",session["user_id"], name, qty, price,date,product,pnl)
        # update the product db with the remainder 
        db.execute("UPDATE products SET qty = ? WHERE rowid = ? AND name LIKE ?;", remainder, session["user_id"], product)
        flash("Invoice created")
        return redirect(url_for("dashboard"))
    else:
        row = db.execute("SELECT * FROM products WHERE rowid = ?;",session["user_id"])
        return render_template("createinvoice.html", products=row)


# remove_product
@app.route("/remove_product", methods = ["GET","POST"])
@login_required
def remove_product():
    # get remove product data
    if request.method == "POST":
        product = request.form.get('products')
        qty = request.form.get('in_quantity')
        # remove finished products from inventory
        row = db.execute("SELECT qty FROM products WHERE rowid = ? AND name = ?;",session["user_id"], product)
        qty1 =row[0]['qty']
        qty = int(qty)
        remainder = (qty1 - qty)
        # update product db with the remainder 
        db.execute("UPDATE products SET qty = ? WHERE rowid = ? AND name LIKE ?;", remainder, session["user_id"], product)
        flash("Product removed")
        return redirect(url_for("dashboard"))
    else:
        row = db.execute("SELECT * FROM products WHERE rowid = ?;",session["user_id"])
        return render_template("remove_product.html", products=row)


# transaction
@app.route("/transaction", methods = ["GET","POST"])
@login_required
def transaction():
        # query db for transaction data and display it 
        row = db.execute("SELECT * FROM sales WHERE rowid = ?;", session['user_id'])
        return render_template("transaction.html", database=row)