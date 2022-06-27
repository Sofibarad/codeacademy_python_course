from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return 5 * render_template("greetings1.html", vardas=vardas)
    else:
        return render_template("login1.html")


if __name__ == "__main__":
    app.run()