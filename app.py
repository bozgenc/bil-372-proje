from flask import Flask, render_template, request,flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="/Users/elifg/PycharmProjects/Bil372Proje/templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/ProjectDB"
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
@app.route('/uretici',  methods=['POST', 'GET'])
def uretici():
    if request.method == "POST":
        ad = request.form['ad']
        soyad = request.form['soyad']
        tckn = request.form['tckn']
        koy = request.form['koy']
        tel_no = request.form['tel_no']

        query = "INSERT INTO \"Uretici\"(ad, soyad, tckn, koy, tel_no) VALUES ('" + ad + "' , '" + soyad + "', '" + tckn + "','" + koy + "','" + tel_no + "')"
        result = db.engine.execute(query)
        db.session.add(result)
        db.session.commit()
        return render_template("uretici.html")
    else:
        all_data = "Select * from public.\"Uretici\""
        result = db.engine.execute(all_data)
        return render_template("uretici.html", feat=result)

@app.route('/satis',  methods=['POST', 'GET'])
def  satis():
    if request.method == "POST":
            ucret = request.form['ucret']
            tarih = request.form['tarih']
            miktar = request.form['miktar']
            alici_sirket_id = request.form['alıcı_sirket_id']

            query = "INSERT INTO \"Satis\"(ucret, tarih, miktar, alici_sirket_id) VALUES ('" + ucret + "' , '" + tarih + "', '" + miktar + "','" + alici_sirket_id + "')"
            result = db.engine.execute(query)
            db.session.add(result)
            db.session.commit()
            return render_template("satis.html")
    else:
            all_data = "Select * from public.\"Satis\""
            result = db.engine.execute(all_data)
            return render_template("satis.html", feat=result)



@app.route("/Satis_delete/<int:id>", methods=['GET','POST'])
def SatisDelete(id):
    if request.method == 'GET':
        query = "DELETE FROM public.\"Satis\" WHERE id = '" + str(id) + "'"
        db.engine.execute(query)

    queryAlici = "SELECT * FROM public.\"Alıcı\""
    temp = db.session.execute(queryAlici)
    #queryArac = "SELECT * FROM public.\"Arac\""
    #temp2 = db.session.execute(queryArac)
    queryAll = "SELECT public.\"Satis\".alici_sirket_id, public.\"Satis\".miktar, public.\"Satin_Alir\".tarih, public.\"Satin_Alir\".ucret,  FROM( public.\"Satis\" INNER JOIN public.\"Alici\" ON public.\"Satis\".alici_sirket_id = public.\"Alici\".sirket_id)"
    temp3 = db.session.execute(queryAll)

    uList = temp.fetchall()
    #aList = temp2.fetchall()
    purchaseList = temp3.fetchall()
    return render_template("satis.html", aliciList=uList, satisList=purchaseList)

if __name__ == "__main__":
    app.debug = True
    app.run()
