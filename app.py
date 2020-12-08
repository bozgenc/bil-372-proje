from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder="/Users/baranozgenc/Desktop/proje/Bil372Proje/templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost:5432/coffeeDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    return render_template("register.html", )


@app.route("/iletisim", methods=['GET', 'POST'])
def iletisim():
    if request.method == 'POST':
        email = request.form['email']
        mesaj = request.form['mesaj']
        if len(mesaj) > 0 or len(email) > 0:

            query = "INSERT INTO \"Iletisim\"(email, mesaj) VALUES ('" + email + "' , '" + mesaj + "')"

            result = db.engine.execute(query)

        else:
            flash("Lütfen alanları doldurun !")

            return render_template("iletisim.html")

    return render_template("iletisim.html", )


@app.route('/cekirdek', methods=['GET', 'POST'])
def cekirdek():
    if request.method == 'POST':
        miktar = request.form['miktar']
        tur = request.form['tur']
        koken = request.form['koken']
        id = request.form['isInsert']

        intMiktar = int(miktar)
        print("id:")
        print(id)

        if int(id) == 0:
            if intMiktar > 0:
                query = "INSERT INTO \"Cekirdek\"(koken, miktar, tur) VALUES ('" + koken + "' , '" + miktar + "', '" + tur + "')"
                result = db.engine.execute(query)
            else:

                flash("Miktar sıfırdan fazla olmalı., lütfen tekrar deneyin!")
                return render_template("cekirdek.html")

        else:

            query_update = "UPDATE public.\"Cekirdek\" SET koken = '" + koken + "', miktar = '" + miktar + "', tur = '" + tur + "' WHERE id = '" + str(

                id) + "'"

            db.engine.execute(query_update)

    queryCekirdek = "SELECT * FROM public.\"Cekirdek\""
    temp = db.session.execute(queryCekirdek)

    cList = temp.fetchall()

    return render_template("cekirdek.html", cekirdekList=cList)


@app.route('/paket', methods=['GET', 'POST'])
def paket():
    if request.method == 'POST':
        gramaj = request.form['gramaj']
        tur = request.form['tur']
        skt = request.form['skt']
        id = request.form['isInsert']

        if int(id) == 0:
            query = "INSERT INTO \"Paket_Kahve\"(gramaj, skt, tur) VALUES ('" + gramaj + "' , '" + skt + "', '" + tur + "')"
            result = db.engine.execute(query)

        else:
            query_update = "UPDATE public.\"Paket_Kahve\" SET tur = '" + tur + "', gramaj = '" + gramaj + "', skt = '" + skt + "' WHERE id = '" + str(
                id) + "'"
            db.engine.execute(query_update)

    queryPaket = "SELECT * FROM public.\"Paket_Kahve\""
    temp = db.session.execute(queryPaket)

    pList = temp.fetchall()

    return render_template("paket.html", paketList=pList)


@app.route("/cekirdek_delete/<int:id>", methods=['GET', 'POST'])
def cekirdekDelete(id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Cekirdek\" WHERE id = '" + str(id) + "'"
        db.engine.execute(query)

    queryPaket = "SELECT * FROM public.\"Cekirdek\""
    temp = db.session.execute(queryPaket)

    cList = temp.fetchall()

    return render_template("paket.html", cekirdekList=cList)


@app.route("/paket_delete/<int:id>", methods=['GET', 'POST'])
def paketDelete(id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Paket_Kahve\" WHERE id = '" + str(id) + "'"
        db.engine.execute(query)

    queryPaket = "SELECT * FROM public.\"Paket_Kahve\""
    temp = db.session.execute(queryPaket)

    pList = temp.fetchall()

    return render_template("paket.html", paketList=pList)


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
            update_query = "UPDATE public.\"Personel\" SET tckn = '" + tckn + "', ad = '" + ad + "', soyad = '" + soyad + "', tel_no = '" + tel_no + "', email = '" + email + "', personel_tipi = '" + personel_tipi + "'  WHERE tckn = '" + str(
                id) + "'"
            db.engine.execute(update_query)

    query = "SELECT * FROM public.\"userTypes\""
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

    query = "SELECT * FROM public.\"userTypes\""
    temp = db.session.execute(query)
    queryPersonel = "SELECT * FROM public.\"Personel\""
    temp2 = db.session.execute(queryPersonel)

    roleList = temp.fetchall()
    personelList = temp2.fetchall()

    return render_template("adminHome.html", roleList=roleList, personelList=personelList)

@app.route("/adminHome_search", methods=['GET', 'POST'])
def admin_search():
    if request.method == 'POST':
        search = request.form['search']

        if search != ' ' or search != '':
            query = "SELECT public.\"Personel\".* FROM public.\"Personel\" INNER JOIN ( SELECT public.\"Personel\".tckn AS pg_search_id,(ts_rank((to_tsvector('english', coalesce(public.\"Personel\".ad::text,  '')) || to_tsvector('english', coalesce(public.\"Personel\".soyad::text, '')) || to_tsvector('english', coalesce(public.\"Personel\".email::text, ''))),(to_tsquery('english', ''' ' || '" + search + "'|| ' ''')))) FROM public.\"Personel\" WHERE (((to_tsvector('english', coalesce(public.\"Personel\".ad::text, '')) ||to_tsvector('english', coalesce(public.\"Personel\".soyad::text, '')) ||to_tsvector('english', coalesce(public.\"Personel\".email::text, ''))) @@ (to_tsquery('english', ''' ' || '"+ search + " '|| ' '''))))) pg_search ON public.\"Personel\".tckn= pg_search.pg_search_id LIMIT 24 OFFSET 0"
            t = db.engine.execute(query)
            list = t.fetchall()
            query = "SELECT * FROM public.\"userTypes\""
            temp = db.session.execute(query)
            queryPersonel = "SELECT * FROM public.\"Personel\""
            temp2 = db.session.execute(queryPersonel)

            roleList = temp.fetchall()
            return render_template("adminHome.html", roleList=roleList, personelList=list, son=list)



@app.route('/satis',  methods=['POST', 'GET'])
def satis():
    if request.method == "POST":
            ucret = request.form['ucret']
            tarih = request.form['tarih']
            miktar = request.form['miktar']
            alici_sirket_id = request.form['alici_sirket_id']
            id = request.form['isInsert']

            if int(id) == 0:
                query = "INSERT INTO public.\"Satis\"(alici_sirket_id,ucret,tarih,miktar) VALUES ('" + alici_sirket_id + "', '" + ucret + "','" + tarih + "','" + miktar + "')"
                db.engine.execute(query)
            else:
                query = "UPDATE public.\"Satis\" SET  alici_sirket_id= '" + alici_sirket_id + "', tarih = '" + tarih + "', ucret = '" + ucret + "', miktar = '" + miktar + "' where alici_sirket_id = '" + alici_sirket_id + "'"
                db.engine.execute(query)

    all_data = "Select * from public.\"Satis\""
    result = db.engine.execute(all_data)
    sList = result.fetchall()
    return render_template("satis.html", satisList=sList)



@app.route("/satis_delete/<int:alici_sirket_id>", methods=['GET','POST'])
def SatisDelete(alici_sirket_id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Satis\" WHERE alici_sirket_id =  alici_sirket_id"
        db.engine.execute(query)

        all_data = "Select * from public.\"Satis\""
        result = db.engine.execute(all_data)
        sList = result.fetchall()
        return render_template("satis.html", satisList=sList)


@app.route('/alici', methods=['POST', 'GET'])
def alici():
    if request.method == "POST":
            sirket_adi = request.form['sirket_adi']
            sirket_id = request.form['sirket_id']

            id = request.form['isInsert']

            if int(id) == 0:
                query = "INSERT INTO \"Alici\"(sirket_adi,sirket_id) VALUES ('" + sirket_adi + "' , '" + sirket_id + "')"
                db.engine.execute(query)
            else:
                query = "UPDATE public.\"Alici\" SET  sirket_id= '" + sirket_id + "', sirket_adi = '" + sirket_adi + "' where sirket_id = '" + sirket_id + "'"
                db.engine.execute(query)

    all_data = "Select * from public.\"Alici\""
    result = db.engine.execute(all_data)
    aList = result.fetchall()
    return render_template("alici.html", aliciList=aList)




@app.route('/alici_delete/<string:sirket_adi>', methods=['GET', 'POST'])
def alici_delete(sirket_adi):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Alici\" where sirket_adi = '" +  sirket_adi + "'"
        db.engine.execute(query)

    all_data = "Select * from public.\"Alici\""
    result = db.engine.execute(all_data)
    uList = result.fetchall()
    return render_template("alici.html", aliciList= uList)




@app.route("/nakliyeciHome", methods=['GET', 'POST'])
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
            insertQuery = "INSERT INTO public.\"Satin_Alir\"(uretici_tckn, odeme_tarihi,aciklama, odeme_miktari ,urun_miktari, plaka) VALUES ('" + uretici_tckn + "' , '" + str(
                today) + "' ,'" + aciklama + "' , '" + odeme + "' ,'" + miktar + "', '" + arac + "')"
            db.engine.execute(insertQuery)

        else:
            query_update = "UPDATE public.\"Satin_Alir\" SET uretici_tckn = '" + uretici_tckn + "', aciklama = '" + aciklama + "', odeme_miktari = '" + odeme + "', odeme_tarihi = '" + str(
                today) + "', urun_miktari = '" + str(miktar) + "', plaka = '" + arac + "'  WHERE id = '" + str(id) + "'"
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
        id = request.form['isInsert']
        boolBittiMi = False;

        if bitti_mi == "True":
            boolBittiMi = True

        if int(id) == 0:
            insertQuery = "INSERT INTO public.\"Kavurma\"(sorumlu_koordinator_tckn, tur_id, giren_miktar, cikan_miktar ,islem_suresi, bitti_mi) VALUES ('" + tckn + "' , '" + tur_id + "' ,'" + giren_miktar + "' , '" + str(
                0) + "' ,'" + str(0) + "', '" + bitti_mi + "')"
            db.engine.execute(insertQuery)
        else:
            query_update = "UPDATE public.\"Kavurma\" SET sorumlu_koordinator_tckn = '" + tckn + "', tur_id = '" + tur_id + "', giren_miktar = '" + giren_miktar + "', cikan_miktar = '" + cikan_miktar + "', islem_suresi = '" + islem_suresi + "', bitti_mi = '" + bitti_mi + "'  WHERE id = '" + str(
                id) + "'"
            db.engine.execute(query_update)

            if boolBittiMi == True:
                queryGet = "SELECT * FROM public.\"Islem_Sonu\""
                resTemp = db.session.execute(queryGet)
                resTemp = resTemp.fetchall()

                flag = True
                for x in resTemp:
                    if x.id3 == id:
                        flag = False
                if flag:
                    queryIslemSonu = "INSERT INTO public.\"Islem_Sonu\"(sorumlu_koordinator_tckn, tur_id, id3) VALUES ('" + tckn + "' , '" + tur_id + "' ,'" + str(
                        id) + "')"
                    db.engine.execute(queryIslemSonu)

    query = "SELECT * FROM public.\"Personel\" WHERE personel_tipi = 'koordinator'"
    res = db.session.execute(query)

    queryJoin = "SELECT public.\"Kavurma\".giren_miktar, public.\"Kavurma\".bitti_mi  ,public.\"Kavurma\".id, public.\"Kavurma\".sorumlu_koordinator_tckn, public.\"Kavurma\".cikan_miktar, public.\"Kavurma\".islem_suresi, public.\"Personel\".ad, public.\"Personel\".soyad FROM (public.\"Kavurma\" INNER JOIN public.\"Personel\" ON public.\"Kavurma\".sorumlu_koordinator_tckn = public.\"Personel\".tckn) WHERE public.\"Kavurma\".bitti_mi = False "
    result = db.session.execute(queryJoin)

    personelList = res.fetchall()
    kavurmaList = result.fetchall()

    return render_template("kavurma.html", personelList=personelList, kavurmaList=kavurmaList)


@app.route("/kavurma_delete/<int:id>", methods=['GET', 'POST'])
def kavurma_delete(id):
    if request.method == 'GET':
        queryDel = "DELETE FROM public.\"Kavurma\" WHERE id = '" + str(id) + "'"
        db.engine.execute(queryDel)

    query = "SELECT * FROM public.\"Personel\" WHERE personel_tipi = 'koordinator'"
    res = db.session.execute(query)

    queryJoin = "SELECT public.\"Kavurma\".giren_miktar, public.\"Kavurma\".bitti_mi  ,public.\"Kavurma\".id, public.\"Kavurma\".sorumlu_koordinator_tckn, public.\"Kavurma\".cikan_miktar, public.\"Kavurma\".islem_suresi, public.\"Personel\".ad, public.\"Personel\".soyad FROM (public.\"Kavurma\" INNER JOIN public.\"Personel\" ON public.\"Kavurma\".sorumlu_koordinator_tckn = public.\"Personel\".tckn) WHERE public.\"Kavurma\".bitti_mi = False "
    result = db.session.execute(queryJoin)

    personelList = res.fetchall()
    kavurmaList = result.fetchall()

    return render_template("kavurma.html", personelList=personelList, kavurmaList=kavurmaList)


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
            query = "UPDATE public.\"Uretici\" SET ad_soyad ='" + ad_soyad + "', tckn = '" + tckn + "', koy = '" + koy + "', tel_no = '" + tel_no + "' where tckn = '" + tckn + "'"
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

        query = "SELECT * from public.\"Personel\" where tckn = '" + sorumlu_koordinator_tckn + "'"
        result = db.session.execute(query)
        result = result.fetchall()
        sorumlu_koordinator_tckn = result[0].tckn

        if int(id) == 0:
            query = "INSERT INTO public.\"Ogutme\"(sorumlu_koordinator_tckn, tur_id, giren_miktar, cikan_miktar, islem_suresi," \
                    "bitti_mi) VALUES ('" + sorumlu_koordinator_tckn + "','" + str(1) + "','" + str(
                giren_miktar) + "','" + \
                    str(0) + "','" + str(0) + "','" + str(bitti_mi) + "')"
            db.session.execute(query)
            db.session.commit()
        else:
            query = "UPDATE public.\"Ogutme\" SET sorumlu_koordinator_tckn = '" + sorumlu_koordinator_tckn + "', tur_id = '" + tur_id + "', giren_miktar = '" + giren_miktar + "', cikan_miktar = '" + cikan_miktar + "', islem_suresi = '" + islem_suresi + "', bitti_mi = '" + bitti_mi + "'  WHERE id = '" + str(
                id) + "'"
            db.session.execute(query)
            db.session.commit()


    query = "SELECT public.\"Ogutme\".giren_miktar, public.\"Ogutme\".bitti_mi  ,public.\"Ogutme\".id, public.\"Ogutme\".sorumlu_koordinator_tckn, public.\"Ogutme\".cikan_miktar, " \
            "public.\"Ogutme\".islem_suresi, public.\"Personel\".ad, public.\"Personel\".soyad FROM (public.\"Ogutme\" INNER JOIN public.\"Personel\" ON public.\"Ogutme\".sorumlu_koordinator_tckn = public.\"Personel\".tckn) " \
            "WHERE public.\"Ogutme\".bitti_mi = False "
    all_data = db.session.execute(query)
    islem_list = all_data.fetchall()

    query2 = "SELECT * from public.\"Personel\" WHERE personel_tipi = 'koordinator'"
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


    return render_template("ogutme.html", ogutme=islem_list, personelList=son)


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

            if len(comp) > 0:
                idmiz = comp[0].id2
                if idmiz != id_meselesi:
                    insertquery = "INSERT INTO public.\"Islem_Sonu\"(sorumlu_koordinator_tckn, tur_id, id2) VALUES ('" + sorumlu_koordinator_tckn + "',' " + str(
                        tur_id) + "','" + str(ogutmeList[0].id) + "')"
                    db.engine.execute(insertquery)

            if len(comp) == 0:
                insertquery = "INSERT INTO public.\"Islem_Sonu\"(sorumlu_koordinator_tckn, tur_id, id2) VALUES ('" + sorumlu_koordinator_tckn + "','" + str(
                    tur_id) + "','" + str(ogutmeList[0].id) + "')"
                db.engine.execute(insertquery)

    q2 = "SELECT public.\"Ogutme\".giren_miktar, public.\"Ogutme\".cikan_miktar, public.\"Ogutme\".islem_suresi, public.\"Personel\".ad, public.\"Personel\".soyad, public.\"Islem_Turu\".islem_ismi FROM(( public.\"Ogutme\" INNER JOIN public.\"Personel\" ON public.\"Ogutme\".sorumlu_koordinator_tckn = public.\"Personel\".tckn) INNER JOIN public.\"Islem_Turu\" ON public.\"Ogutme\".tur_id = public.\"Islem_Turu\".tur_id)"
    data = db.session.execute(q2)


    q3 = "SELECT public.\"Kavurma\".giren_miktar, public.\"Kavurma\".cikan_miktar, public.\"Kavurma\".islem_suresi, public.\"Personel\".ad, public.\"Personel\".soyad, public.\"Islem_Turu\".islem_ismi FROM(( public.\"Kavurma\" INNER JOIN public.\"Personel\" ON public.\"Kavurma\".sorumlu_koordinator_tckn = public.\"Personel\".tckn) INNER JOIN public.\"Islem_Turu\" ON public.\"Kavurma\".tur_id = public.\"Islem_Turu\".tur_id)"
    res = db.session.execute(q3)
    list2 = res.fetchall()
    islem_sonu_list = data.fetchall()

    listFinal = list2 + islem_sonu_list
    return render_template("islem_sonu.html", data=listFinal)


@app.route('/araclar', methods=['GET', 'POST'])
def araclar():
    if request.method == 'POST':
        plaka = request.form['plaka']
        kapasite = request.form['kapasite']
        id = request.form['isInsert']

        if int(id) == 0:
            query = "INSERT INTO public.\"Arac\"(plaka, kapasite) VALUES ('" + plaka + "' , '" + kapasite + "')"
            db.engine.execute(query)
        else:
            queryUpdate = "UPDATE public.\"Arac\" SET kapasite = '" + kapasite + "'" + " WHERE id = '" + str(id) + "'"
            db.engine.execute(queryUpdate)

    queryAraclar = "SELECT * FROM public.\"Arac\""
    res = db.session.execute(queryAraclar)
    aracList = res.fetchall()

    return render_template("araclar.html", aracList=aracList)


@app.route('/araclar_delete/<int:id>', methods=['GET', 'POST'])
def araclar_delete(id):
    if request.method == 'GET':
        queryDel = "DELETE FROM public.\"Arac\" WHERE id = '" + str(id) + "'"
        db.engine.execute(queryDel)

    queryAraclar = "SELECT * FROM public.\"Arac\""
    res = db.session.execute(queryAraclar)
    aracList = res.fetchall()

    return render_template("araclar.html", aracList=aracList)


@app.route("/")
def home():
    return render_template("homePage.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
