from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="/Users/baranozgenc/Desktop/proje/Bil372Proje/templates")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost:5432/projeDB"
db = SQLAlchemy(app)


@app.route("/register", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tckn = request.form['tckn']
        password = request.form['password']
        password2 = request.form['password2']

        roleQuery = "SELECT * FROM personel WHERE tckn =  '" + tckn + "' "
        temp = db.session.execute(roleQuery)
        userType = ""
        for x in temp:
            userType = x.userrole

        if password == password2:
            query = "INSERT INTO Login(tckn, passcode, userRole) VALUES ('" + tckn + "' , '" + password + "', '" + userType + "')"
            result = db.engine.execute(query)

    return render_template("register.html",)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/page1")
def page1():
    return render_template("page1.html")


if __name__ == "__main__":
    app.debug = True
    app.run()