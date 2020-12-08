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
            query2 = "UPDATE public.\"Islem_Turu\" SET islem_ismi = '" + islem_ismi + "'" + " WHERE tur_id = '" + str(
                tur_id) + "'"
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
        giren_miktar = request.form['giren_miktar']
        cikan_miktar = request.form['cikan_miktar']
        islem_suresi = request.form['islem_suresi']
        bitti_mi = request.form['bitti_mi']
        id = request.form['isInsert']
        tur_id = "1"
        print(giren_miktar)
        query = "SELECT * from public.\"Personel\" where tckn = '" + sorumlu_koordinator_tckn + "'"
        result = db.session.execute(query)
        result = result.fetchall()
        sorumlu_koordinator_tckn = result[0].tckn

        if int(id) == 0:
            query = "INSERT INTO public.\"Ogutme\"(sorumlu_koordinator_tckn, tur_id, giren_miktar, cikan_miktar, islem_suresi," \
                    "bitti_mi) VALUES ('" + sorumlu_koordinator_tckn + "','" + str(1) + "','" + str(giren_miktar) + "','" + \
                    str(0) + "','" + str(0) + "','" + str(bitti_mi) + "')"
            db.session.execute(query)
            db.session.commit()
        else:
            query = "UPDATE public.\"Ogutme\" SET sorumlu_koordinator_tckn = '" + sorumlu_koordinator_tckn + "', tur_id = '" + tur_id + "', giren_miktar = '" + giren_miktar + "', cikan_miktar = '" + cikan_miktar + "', islem_suresi = '" + islem_suresi + "', bitti_mi = '" + bitti_mi + "'  WHERE id = '" + str(id) + "'"
            db.session.execute(query)
            db.session.commit()

    query = "SELECT * FROM public.\"Ogutme\""
    all_data = db.session.execute(query)
    islem_list = all_data.fetchall()

    query2 = "SELECT * from public.\"Personel\""
    data = db.session.execute(query2)
    son = data.fetchall()

    return render_template("ogutme.html", ogutme=islem_list, personelList=son)


@app.route("/ogutme_delete/<int:id>", methods=['GET', 'POST'])
def ogutme_delete(id):
    if request.method == 'GET':
        query = "DELETE from public.\"Ogutme\" where id = '" + str(id) + "'"
        db.engine.execute(query)

    query = "SELECT * FROM public.\"Ogutme\""
    all_data = db.session.execute(query)
    islem_list = all_data.fetchall()

    query2 = "SELECT * from public.\"Personel\""
    data = db.session.execute(query2)
    son = data.fetchall()

    query3 = "SELECT * FROM public.\"Islem_Turu\""
    all_data2 = db.session.execute(query3)
    islemlist = all_data2.fetchall()

    return render_template("ogutme.html", ogutme=islem_list, personelList=son, islemList=islemlist)


@app.route("/islem_sonu", methods=['GET', 'POST'])
def islem_sonu():
    if request.method == 'GET':

        query = "SELECT * from public.\"Ogutme\" where bitti_mi = '" + str(True) + "'"
        all_data = db.engine.execute(query)
        ogutmeList = all_data.fetchall()

        if len(ogutmeList) > 0:
            sorumlu_koordinator_tckn = ogutmeList[0].sorumlu_koordinator_tckn
            tur_id = ogutmeList[0].tur_id
            id_meselesi = ogutmeList[0].id

            quer = "Select * from public.\"Islem_Sonu\""
            comp = db.engine.execute(quer)
            comp = comp.fetchall()
            print(comp)

            if len(comp) > 0:
                print(ogutmeList)
                print(ogutmeList[0].giren_miktar)
                print(ogutmeList[0].id)
                idmiz = comp[0].id2

                if idmiz != id_meselesi:
                    insertquery = "INSERT INTO public.\"Islem_Sonu\"(sorumlu_koordinator_tckn, tur_id, id2) VALUES ('" + sorumlu_koordinator_tckn + "',' " + str(tur_id) + "','" + str(ogutmeList[0].id) + "')"
                    db.engine.execute(insertquery)

            if len(comp) == 0:
                insertquery = "INSERT INTO public.\"Islem_Sonu\"(sorumlu_koordinator_tckn, tur_id, id2) VALUES ('" + sorumlu_koordinator_tckn + "','" + str(tur_id) + "','" + str(ogutmeList[0].id) + "')"
                db.engine.execute(insertquery)

    q2 = "SELECT public.\"Ogutme\".sorumlu_koordinator_tckn, public.\"Ogutme\".tur_id, public.\"Ogutme\".giren_miktar, public.\"Ogutme\".cikan_miktar, public.\"Ogutme\".islem_suresi, " \
         "public.\"Islem_Sonu\".tur_id from public.\"Ogutme\", public.\"Islem_Sonu\" where(public.\"Ogutme\".tur_id = public.\"Islem_Sonu\".tur_id and public.\"Ogutme\".bitti_mi = True)"
    data = db.session.execute(q2)
    islem_sonu_list = data.fetchall()
    return render_template("islem_sonu.html", data=islem_sonu_list)


if __name__ == "__main__":
    app.debug = True
    app.run()
