from flask import Flask, render_template, request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists

app = Flask(__name__, template_folder="C:\\Users\\user\\Documents\\GitHub\\Bil372Proje\\templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:vampirler@localhost:5432/dbV4"
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

    return render_template("register.html",)



@app.route("/iletisim", methods=['GET', 'POST'])
def iletisim():
    if request.method == 'POST':
        email = request.form['email']
        mesaj = request.form['mesaj']
        if len(mesaj) >0 or  len(email) >0:

            query = "INSERT INTO \"Iletisim\"(email, mesaj) VALUES ('" + email + "' , '" + mesaj +  "')"

            result = db.engine.execute(query)

        else:
            flash("Lütfen alanları doldurun !")

            return render_template("iletisim.html")


    return render_template("iletisim.html",)



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
            query_update = "UPDATE public.\"Paket_Kahve\" SET tur = '" + tur + "', gramaj = '" + gramaj + "', skt = '"+ skt +"' WHERE id = '" + str(id) + "'"
            db.engine.execute(query_update)




    queryPaket = "SELECT * FROM public.\"Paket_Kahve\""
    temp = db.session.execute(queryPaket)

    pList = temp.fetchall()

    return render_template("paket.html", paketList=pList)






@app.route("/cekirdek_delete/<int:id>", methods=['GET','POST'])
def cekirdekDelete(id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Cekirdek\" WHERE id = '" + str(id) + "'"
        db.engine.execute(query)

    queryPaket = "SELECT * FROM public.\"Cekirdek\""
    temp = db.session.execute(queryPaket)

    cList = temp.fetchall()

    return render_template("paket.html", cekirdekList=cList)










@app.route("/paket_delete/<int:id>", methods=['GET','POST'])
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
                #else:
                    #return render_template("admin.html")
    else:
        return render_template("login.html")











@app.route("/")
def home():
    return render_template("index.html")











if __name__ == "__main__":
    app.debug = True
    app.run()