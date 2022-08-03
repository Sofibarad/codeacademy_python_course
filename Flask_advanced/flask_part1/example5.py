from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name_from_form = request.form['name']
        return render_template("greetings1.html", name=name_from_form)
    else:
        return render_template("login1.html")
    
    
if __name__ == "__main__":
    app.run()