from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="/Users/Lenovo/Bil372Proje/templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@127.0.0.1:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/register", methods=['GET', 'POST'])
def register():
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

    return render_template("register.html", )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tckn = request.form['tckn']
        password = request.form['password']
        passwordFlag = False

        query = "SELECT * FROM login WHERE tckn =  '" + tckn + "' "
        temp = db.session.execute(query)
        rows = temp.fetchall()

        if len(rows) == 0:
            flash("No user found in the database with the TCKN " + tckn, 'error')
            return render_template("login.html")
        else:
            userrole = rows[0].userrole
            if password == rows[0].passcode:
                passwordFlag = True
            if passwordFlag:
                if userrole == "koordinator":
                    return render_template("index.html")
                elif userrole == "nakliyeci":
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


@app.route("/islemturu", methods=['GET', 'POST'])
def islem_turu():
    if request.method == 'POST':
        tur_id = request.form['tur_id']
        islem_ismi = request.form['islem_ismi']
        id = request.form['isInsert']

        if not None and int(id) == 0:
            query = "INSERT INTO public.\"Islem_Turu\"(tur_id, islem_ismi) VALUES ('" + tur_id + "','" + islem_ismi + "')"
            db.session.execute(query)
            db.session.commit()
        else:
            print(id)
            query2 = "UPDATE public.\"Islem_Turu\" SET tur_id ='" + tur_id + "', islem_ismi = '" + islem_ismi + "'" + " WHERE tur_id = '" + str(tur_id) + "'"
            db.session.execute(query2)
            db.session.commit()

    query = "SELECT * FROM public.\"Islem_Turu\""
    all_data = db.session.execute(query)
    islem_list = all_data.fetchall()

    return render_template("islemturu.html", islem_listesi=islem_list)


@app.route("/islem_turu_delete/<int:tur_id>", methods=['GET', 'POST'])
def islem_turu_delete(tur_id):
    if request.method == 'GET':
        query = "DELETE from public.\"Islem_Turu\" where tur_id = '" + str(tur_id) + "'"
        db.engine.execute(query)

    all_data = "Select * from public.\"Islem_Turu\""
    result = db.session.execute(all_data)
    islem_listesi = result.fetchall()

    return render_template("islemturu.html", islem_listesi=islem_listesi)


@app.route("/ogutme", methods=['GET', 'POST'])
def ogutme():
    if request.method == 'POST':
        sorumlu_koordinator_tckn = request.form['sorumlu_koordinator_tckn']
        tur_id = request.form['tur_id']
        giren_miktar = request.form['giren_miktar']
        cikan_miktar = request.form['cikan_miktar']
        islem_suresi = request.form['islem_suresi']
        bitti_mi = request.form['bitti_mi']
        id = request.form['isInsert']

        query = "SELECT * from public.\"Personel\" where tckn = '" + sorumlu_koordinator_tckn + "'"
        result = db.session.execute(query)
        result = result.fetchall()
        sorumlu_koordinator_tckn = result[0].tckn

        query2 = "SELECT * from public.\"Islem_Turu\" where tur_id = '" + tur_id + "'"
        res = db.session.execute(query2)
        res = result.fetchall()
        tur_id = res[0].tur_id

        if id == "0":
            query = "INSERT INTO public.\"Islem_Turu\"(sorumlu_koordinator_tckn, tur_id) VALUES ('" + sorumlu_koordinator_tckn + "','" + tur_id + "')"
            db.session.execute(query)
            db.session.commit()
        else:
            query = "update"

    query = "SELECT * FROM public.\"Ogutme\""
    all_data = db.session.execute(query)
    islem_list = all_data.fetchall()

    query2 = "SELECT * from public.\"Personel\""
    result = db.session.execute(query2)
    result = result.fetchall()

if __name__ == "__main__":
    app.debug = True
    app.run()
