from flask import Flask

app = Flask(__name__)

@app.route("/")
# dekoratorius 

def home():    
    return "<h1>Čia mano naujas puslapis </h1>"
if __name__ == "__main__":
    app.run(debug=True)