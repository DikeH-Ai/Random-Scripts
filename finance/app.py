import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get the current cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
    reg = list()
    sym = db.execute("SELECT DISTINCT(symbol) FROM userfunc;")
    total = db.execute(" SELECT SUM(shares * price) FROM userfunc WHERE users_id = ?;", session["user_id"])
    # if sym is not empty
    if sym:
        if total[0]["SUM(shares * price)"] is not None:
            # loop through the different symbols & append query result to reg list
            for i in sym:
                info = db.execute(
                    "SELECT SUM(shares), name , price, SUM(shares) * price,symbol FROM userfunc WHERE symbol = ?;", i["symbol"])
                reg.append(info)
            # get cash, total and total2 through an sql query
            cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
            total2 = cash[0]["cash"] + total[0]["SUM(shares * price)"]
            # loop through the size of reg & return updated info each time
            for j in range(len(reg)):
                return render_template("index.html", info=reg, count=j, cash=usd(cash[0]["cash"]), total=usd(total2))
        else:
            defaultcash = cash[0]["cash"]
            return render_template("index.html", info=reg, total=usd(defaultcash), cash=usd(defaultcash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # gather userinputs & check conditions
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Invalid symbol", 400)
        symlook = lookup(symbol)
        if not symlook:
            return apology("Invalid symbol", 400)
        if not shares:
            return apology("Invalid symbol", 400)
        if not shares.isnumeric():
            return apology("Invalid shares", 400)
        if not symbol.isalpha():
            return apology("Invalid symbol", 400)
        shares = float(shares)
        if (shares <= 0):
            return apology("Invalid shares", 400)
        # get cash value
        cash = db.execute("SELECT cash FROM users WHERE CAST(cash AS INT) AND id = ?;", session["user_id"])
        cash = list(cash[0].values())
        # get value of share price
        sharesprice = float(shares * symlook["price"])
        # current time object
        current = datetime.now()
        currentdate = current.strftime("%d-%m-%y %H:%M:%S")
        # if the cash can purchase the comodity, go ahead
        if (sharesprice < cash[0]):
            newcash = cash[0] - sharesprice
            # update the database % render the result
            db.execute("UPDATE users SET cash = ? WHERE id = ?;", newcash, session["user_id"])
            buyer = db.execute("INSERT INTO userfunc(users_id,symbol,shares,price,name, date) VALUES(?,?,?,?,?,?);", int(
                session["user_id"]), symlook["symbol"], shares, symlook["price"], symlook["name"], currentdate)
            sumshares = db.execute("SELECT SUM(shares) FROM userfunc WHERE users_id = ?;", int(session["user_id"]))
            sumshares = list(sumshares[0].values())
            flash("Bought!")
            return redirect("/")
        else:
            return apology("Can't afford", 400)

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Query database info & print them using a jinja loop
    history = db.execute("SELECT * FROM userfunc WHERE users_id = ?;", session["user_id"])
    return render_template("history.html", his=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # if the request is "post"
    if request.method == "POST":
        # getinput symbol
        syb = request.form.get("symbol")
        # use lookup function on the getinput
        result = lookup(syb)
        # print price on sucessful lookup or print apology
        if result:
            dollars = usd(result["price"])
            return render_template("postquote.html", result=result, dollars=dollars)
        else:
            return apology("Invaild symbol", 400)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # gather user inputs
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    if request.method == "POST":
        # cheeck conditiions
        if password != confirmation:
            return apology("two passwords must be the same")
        if not username:
            return apology("must provide username", 400)
        if not password:
            return apology("must provide password", 400)
        userdb = db.execute("SELECT * FROM users WHERE username = ? ;", username)
        if len(userdb) > 0:
            return apology("Username alreay exist")
        # insert into database & set session id
        hashpass = generate_password_hash(password)
        userupdate = db.execute("INSERT INTO users(username,hash) VALUES (?,?);", username, hashpass)
        userdb1 = db.execute("SELECT * FROM users WHERE username = ? ;", username)
        session["user_id"] = userdb1[0]["id"]
        flash("Registered")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Only one symbol need to represent all the shares. Query of unique symbols
    symbols = db.execute(
        "SELECT DISTINCT(symbol) FROM userfunc GROUP BY symbol HAVING users_id = ? AND SUM(shares) != 0 ;", session["user_id"])
    # gather userinput and check conditions
    if request.method == "POST":
        sym = request.form.get("symbol")
        shares = request.form.get("shares")
        shares = int(shares)
        if not sym or (not shares):
            return apology("Missing symbol or shares", 400)
        check = list()
        for value in symbols:
            check.append(value)
        if sym in check[0]:
            return apology("Invalid symbol")
        sharesdb = db.execute("SELECT SUM(shares) FROM userfunc WHERE symbol = ? AND users_id = ?", sym, session["user_id"])
        sharesdb = list(sharesdb[0].values())
        try:
            if shares > sharesdb[0]:
                return apology("Invalid shares", 400)
        except:
            return apology("Invalid shares", 400)
        # current time object
        current = datetime.now()
        currentdate = current.strftime("%d-%m-%y %H:%M:%S")
        # since its a sell order "-"
        shares1 = (-shares)
        current = lookup(sym)
        # insert the new order & modify the total and cash
        seller = db.execute("INSERT INTO userfunc(users_id,symbol,shares,price,name,date) VALUES(?,?,?,?,?,?);",
                            session["user_id"], sym, shares1, current["price"], current["name"], currentdate)
        newcash = current["price"] * shares
        prevcash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
        value = list(prevcash[0].values())
        newcash = newcash + int(value[0])
        db.execute("UPDATE users SET cash = ?  WHERE id = ?;", newcash, session["user_id"])
        flash("Sold!")
        return redirect("/")
    else:
        return render_template("sell.html", symbols=symbols)


@app.route("/topup", methods=["GET", "POST"])
@login_required
def topup():
    # if post, get user input and check conditions
    if request.method == "POST":
        amount = int(request.form.get("topup"))
        if amount < 1:
            return apology("Invalid Amount", 403)
        # get curent cash, add that to topup cash
        row = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
        currentcash = amount + row[0]["cash"]
        # update database
        db.execute("UPDATE users SET cash = ?;", currentcash)
        flash("Toped-Up!")
        return redirect("/")
    else:
        return render_template("topup.html")