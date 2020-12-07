from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__, template_folder="/Users/Lenovo/Bil372Proje/templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@127.0.0.1:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# db = SQLAlchemy(app, engine_options={"pool_pre_ping": True})

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        tckn = request.form['tckn']
        password = request.form['password']
        password2 = request.form['password2']

        roleQuery = "SELECT * FROM public.\"Personel\" WHERE tckn =  '" + tckn + "' "
        print(roleQuery)
        temp = db.session.execute(roleQuery)
        userType = ""
        for x in temp:
            userType = x.personel_tipi

        if password == password2:
            query = "INSERT INTO \"Login\"(tckn, passcode, personel_tipi) VALUES ('" + tckn + "' , '" + password + "', '" + userType + "')"
            result = db.engine.execute(query)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tckn = request.form['tckn']
        password = request.form['password']
        passwordFlag = False

        query = "SELECT * FROM public.\"Login\" WHERE tckn =  '" + tckn + "' "
        temp = db.session.execute(query)
        rows = temp.fetchall()

        if len(rows) == 0:
            flash("No user found in the database with the TCKN " + tckn, 'error')
            return render_template("login.html")
        else:
            personel_tipi = rows[0].personel_tipi
            if password == rows[0].passcode:
                passwordFlag = True
            if passwordFlag:
                if personel_tipi == "koordinator":
                    return render_template("index.html")
                elif personel_tipi == "nakliyeci":
                    return render_template("nakliyeciHome.html")
            else:
                flash("Password is incorrect, please try again!")
                return render_template("login.html")
                # else:
                # return render_template("admin.html")
    else:
        return render_template("login.html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/uretici', methods=['POST', 'GET'])
def uretici():
    if request.method == "POST":
        ad_soyad = request.form['ad_soyad']
        tckn = request.form['tckn']
        koy = request.form['koy']
        tel_no = request.form['tel_no']
        id = request.form['isInsert']

        if int(id) == 0:
            query = "INSERT INTO public.\"Uretici\"(ad_soyad, tckn, koy, tel_no) VALUES ('" + ad_soyad + "', '" + tckn + "','" + koy + "','" + tel_no + "')"
            db.engine.execute(query)
        else:
            query = "UPDATE public.\"Uretici\" SET ad_soyad '" + ad_soyad + "', tckn = '" + tckn + "', koy = '" + koy + "', tel_no = '" + tel_no + "'"
            db.engine.execute(query)

    all_data = "Select * from public.\"Uretici\""
    result = db.engine.execute(all_data)
    uList = result.fetchall()
    return render_template("uretici.html", ureticiList=uList)


@app.route('/uretici_delete/<string:tckn>', methods=['GET', 'POST'])
def uretici_delete(tckn):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Uretici\" where tckn = '" + tckn + "'"
        db.engine.execute(query)

    all_data = "Select * from public.\"Uretici\""
    result = db.engine.execute(all_data)
    uList = result.fetchall()
    return render_template("uretici.html", ureticiList=uList)


if __name__ == "__main__":
    app.debug = True
    app.run()
