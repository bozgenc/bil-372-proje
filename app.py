from flask import Flask, render_template

app = Flask(__name__, template_folder="/Users/baranozgenc/Desktop/proje/Bil372Proje/templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/page1")
def page1():
    return render_template("page1.html")


if __name__ == "__main__":
    app.debug = True
    app.run()