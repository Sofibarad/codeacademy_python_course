from flask import Flask, request, render_template
app = Flask(__name__)

def ar_keliamieji(x:int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

@app.route("/leap", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        year = int(request.form['year'])
        return render_template("greetings4.html", year=year)
        if year is True:
            year = "This is a leap year"
        else:
            year = "This is not leap year"
    else:
        return render_template("login4.html")


if __name__ == "__main__":
    app.run()