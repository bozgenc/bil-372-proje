from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__, template_folder="/Users/baranozgenc/Desktop/proje/Bil372Proje/templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost:5432/coffeeDB"
db = SQLAlchemy(app)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        tckn = request.form['tckn']
        password = request.form['password']
        password2 = request.form['password2']

        roleQuery = "SELECT * FROM public.\"Personel\" WHERE tckn =  '" + tckn + "' "
        temp = db.session.execute(roleQuery)
        rows = temp.fetchall()

        if len(rows) == 0:
            flash("No personel found to be register with the TCKN: " + tckn, 'error')
            return render_template("register.html")
        else:
            userType = rows[0].personel_tipi
            if password == password2:
                query = "INSERT INTO public.\"Login\"(tckn, passcode, personel_tipi) VALUES ('" + tckn + "' , '" + password + "', '" + userType + "')"
                result = db.engine.execute(query)
                if result:
                    flash("Successfully registered, you can log in.")
                    return render_template("login.html")

    return render_template("register.html",)


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
            userrole = rows[0].personel_tipi
            if password == rows[0].passcode:
                passwordFlag = True
            if passwordFlag:
                if userrole == "koordinator":
                    return redirect(url_for("kavurma"), code=303)
                elif userrole == "nakliyeci":
                    return redirect(url_for("nakliyeciHome"), code=303)
                elif userrole == 'admin':
                    return redirect(url_for("adminHome"), code=303)
            else:
                flash("Password is incorrect, please try again!")
                return render_template("login.html")

    else:
        return render_template("login.html")


@app.route("/adminHome", methods=['GET', 'POST'])
def adminHome():
    if request.method == 'POST':
        tckn = request.form['tckn']
        ad = request.form['ad']
        soyad = request.form['soyad']
        tel_no = request.form['tel_no']
        email = request.form['email']
        personel_tipi = request.form['type']
        id = request.form['isInsert']

        if int(id) == 0:
            insertQuery = "INSERT INTO public.\"Personel\"(tckn, ad, soyad, tel_no, email, personel_tipi) VALUES ('" + tckn + "','" + ad + "','" + soyad + "', '" + tel_no + "' , '" + email + "', '" + personel_tipi + "')"
            db.engine.execute(insertQuery)
        else:
            update_query = "UPDATE public.\"Personel\" SET tckn = '" + tckn + "', ad = '" + ad + "', soyad = '" + soyad + "', tel_no = '" + tel_no + "', email = '" + email + "', personel_tipi = '" + personel_tipi + "'  WHERE tckn = '" + str(id) + "'"
            db.engine.execute(update_query)



    query = "SELECT * FROM usertypes"
    temp = db.session.execute(query)
    queryPersonel = "SELECT * FROM public.\"Personel\""
    temp2 = db.session.execute(queryPersonel)

    roleList = temp.fetchall()
    personelList = temp2.fetchall()

    return render_template("adminHome.html", roleList=roleList, personelList=personelList)

@app.route("/adminHome_delete/<int:id>")
def adminHomeDelete(id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Login\" WHERE tckn = '" + str(id) + "'"
        db.engine.execute(query)
        query2 = "DELETE FROM public.\"Personel\" WHERE tckn = '" + str(id) + "'"
        db.engine.execute(query2)

    query = "SELECT * FROM usertypes"
    temp = db.session.execute(query)
    queryPersonel = "SELECT * FROM public.\"Personel\""
    temp2 = db.session.execute(queryPersonel)

    roleList = temp.fetchall()
    personelList = temp2.fetchall()

    return render_template("adminHome.html", roleList=roleList, personelList=personelList)



@app.route("/nakliyeciHome", methods=['GET','POST'])
def nakliyeciHome():
    if request.method == 'POST':
        uretici = request.form['uretici']
        aciklama = request.form['aciklama']
        miktar = request.form['miktar']
        arac = request.form['arac']
        odeme = request.form['odeme']
        id = request.form['isInsert']

        query = "SELECT * FROM public.\"Uretici\" WHERE ad_soyad =  '" + uretici + "'"
        res = db.session.execute(query)
        res = res.fetchall()
        uretici_tckn = res[0].tckn
        today = datetime.today()

        if int(id) == 0:
            insertQuery = "INSERT INTO public.\"Satin_Alir\"(uretici_tckn, odeme_tarihi,aciklama, odeme_miktari ,urun_miktari, plaka) VALUES ('" + uretici_tckn + "' , '" + str(today) + "' ,'" + aciklama + "' , '" + odeme + "' ,'" + miktar + "', '" + arac + "')"
            db.engine.execute(insertQuery)

        else:
            query_update = "UPDATE public.\"Satin_Alir\" SET uretici_tckn = '" + uretici_tckn + "', aciklama = '" + aciklama + "', odeme_miktari = '" + odeme + "', odeme_tarihi = '" + str(today) + "', urun_miktari = '" + str(miktar) + "', plaka = '" + arac + "'  WHERE id = '" + str(id) + "'"
            db.engine.execute(query_update)


    queryUretici = "SELECT * FROM public.\"Uretici\""
    temp = db.session.execute(queryUretici)
    queryArac = "SELECT * FROM public.\"Arac\""
    temp2 = db.session.execute(queryArac)
    queryAll = "SELECT public.\"Satin_Alir\".id, public.\"Satin_Alir\".odeme_miktari, public.\"Satin_Alir\".odeme_tarihi, public.\"Satin_Alir\".urun_miktari, public.\"Satin_Alir\".aciklama, public.\"Satin_Alir\".plaka, public.\"Uretici\".ad_soyad FROM( public.\"Satin_Alir\" INNER JOIN public.\"Uretici\" ON public.\"Satin_Alir\".uretici_tckn = public.\"Uretici\".tckn)"
    temp3 = db.session.execute(queryAll)

    uList = temp.fetchall()
    aList = temp2.fetchall()
    purchaseList = temp3.fetchall()
    return render_template("nakliyeciHome.html", ureticiList=uList, aracList=aList, purchaseList=purchaseList)


@app.route("/nakliyeciHome_delete/<int:id>", methods=['GET', 'POST'])
def nakliyeciHomeDelete(id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Satin_Alir\" WHERE id = '" + str(id) + "'"
        db.engine.execute(query)

    queryUretici = "SELECT * FROM public.\"Uretici\""
    temp = db.session.execute(queryUretici)
    queryArac = "SELECT * FROM public.\"Arac\""
    temp2 = db.session.execute(queryArac)
    queryAll = "SELECT public.\"Satin_Alir\".id, public.\"Satin_Alir\".odeme_miktari, public.\"Satin_Alir\".odeme_tarihi, public.\"Satin_Alir\".urun_miktari, public.\"Satin_Alir\".aciklama, public.\"Satin_Alir\".plaka, public.\"Uretici\".ad_soyad FROM( public.\"Satin_Alir\" INNER JOIN public.\"Uretici\" ON public.\"Satin_Alir\".uretici_tckn = public.\"Uretici\".tckn)"
    temp3 = db.session.execute(queryAll)

    uList = temp.fetchall()
    aList = temp2.fetchall()
    purchaseList = temp3.fetchall()
    return render_template("nakliyeciHome.html", ureticiList=uList, aracList=aList, purchaseList=purchaseList)


@app.route("/kavurma", methods=['GET', 'POST'])
def kavurma():
    if request.method == 'POST':
        tckn = request.form['sorumlu_koordinator_tckn']
        giren_miktar = request.form['giren_miktar']
        cikan_miktar = request.form['cikan_miktar']
        islem_suresi = request.form['islem_suresi']
        bitti_mi = request.form['bitti_mi']
        tur_id = "2"

        insertQuery = "INSERT INTO public.\"Kavurma\"(sorumlu_koordinator_tckn, tur_id, giren_miktar, cikan_miktar ,islem_suresi, bitti_mi) VALUES ('" + tckn + "' , '" + tur_id + "' ,'" + giren_miktar + "' , '" + cikan_miktar + "' ,'" + islem_suresi + "', '" + bitti_mi + "')"
        db.engine.execute(insertQuery)

    query = "SELECT * FROM public.\"Personel\" WHERE personel_tipi = 'koordinator'"
    res = db.session.execute(query)

    queryKavurma = "SELECT * FROM public.\"Kavurma\""
    result = db.session.execute(queryKavurma)

    personelList = res.fetchall()
    kavurmaList = result.fetchall()

    return render_template("kavurma.html", personelList=personelList, kavurmaList=kavurmaList)



@app.route("/")
def home():
    return render_template("homePage.html")


if __name__ == "__main__":
    app.debug = True
    app.run()