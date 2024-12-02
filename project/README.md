# InventX
#### Video Demo:  <https://youtu.be/zKTCRDSm0Sk>
#### Description:
*A simple Inventory management web-application*<br>
---
## Table of Contents  	
---
- Introduction
- Features
- Feedback

---
## Introduction
---
InventX is a simple inventory management web-application for keeping track of sales, income, inventory management and inventory levels. InventX is designed for users who have very little experience with technology and no prior knowledge of how to use an inventory management system. You can carry out operations like creating invoices, viewing your sales history, automatically calculating cumulative income, storing and keeping track of inventory as briefly as possible while being accessible to all devices.

---
## Features
---
- Sale tracking.
- Income tracking.
- Inventory levels tracking.
- Inventory management.
- Security. 

---
## Files & Functions
---
### Template Files
- layout:<br>
    The layout file, which is an HTML file that combines HTML and Jinja, includes the design blueprint for all of the webpages in the web application. <br>
    - head tag<br>
        This holds the meta-data, viewport attribute, bootstrap CDN links and styles.
    - body tag<br>
        This holds the header tag, main tag, footer tag, jinja templates, flash script and nav html link.
- nav:<br>
    The nav file, which is an HTML file that combines HTML and Jinja, is responsible for navigation through all of the webpages in the web application. <br>
     - mult <br>
        This javascript function that performs basic arithmetics. 
    - form tag <br>
        Collects and submits user-input.
    - link tag <br>
        Links to different functions in the app.py file. 
- login: <br>
    The login file contains HTML and Jinja, it displays the login form.
    - form tag<br>
       Collects and submits user-input.
- register:<br>
    The register file contains HTML and Jinja, it displays the register form.
    - form tag<br>
       Collects and submits user-input.
- dashboard:<br>
    The dashboard file contains HTML and Jinja code, it displays information that includes; NAME, EMAIL, USER_ID, TOTAL PRODUCT SALES, TOTAL PRODUCT IN INVENTORY AND TOTAL INCOME.
- transaction:<br>
    The transaction file contains HTML and Jinja code, it displays the full list of sales.  
- createinvoice:<br>
    The createinvoice file contains HTML and Jinja code, responsible for creating new invoice.
    - myfunc <br>
        This javascript function that performs basic arithmetics.
    - form tag<br>
        Collects and submits user-input .
- remove_product
    The remove_product file contains HTML and Jinja code, responsible for removing products.
       - form tag<br>
        Collects and submits user-input. 
### SQL FILE
- myinvent: <br>
    Contains database that keeps track of user information, where inventx functions can be managed or performed.
    - credentials table<br>
        Holds user credentials for easy login, logout and session identification.
    - sales table<br>
        Holds list of sales or invoices created.
    - products table<br>
        Holds list of products added to the database. 
### Flask APP
- app:<br>
    The app file is a Python file that contains Python code that enables all functions to be performed in the web application.
    - imports<br>
        list of imports includes; cs50, flask, flask-session, werkzeug.security, datetime, functools.
    - login_required function<br>
        Handles client access to certain webpages.
    - register function<br>
        Handles client registration.
    - login function<br>
        Handles client login.
    - logout functions<br>
        Handles client logout.
    - dashboard<br>
        Displays dashboard and its contents to client.
    - home function<br>
        Redirects client to dashboard if logged in.
    - Add_product function<br>
       Adds product to the database.
    - createinvoice function<br>
        Handle product sales.
    - removeproduct function<br>
        Handles product removal from inventory. 
    - transaction function<br>
        Handles list of all sales.