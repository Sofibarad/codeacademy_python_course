from flask import Flask, render_template
from dictionary import data


# iš flask bibliotekos importuojame klasę Flask ir f-ją render_template.
app = Flask(__name__)
# inicijuojame klasės Flask objektą, priskiriame kintamąjam app.

@app.route('/')
# įvelkame f-ją į flask dekoratorių. Be jo  funkcija būtų bereikšmė. Dekorato riaus parametruose nurodome, kad norėsime rezultato 127.0.0.1:8000/ url adrese."""

def index():
    return render_template('index1.html', data=data)
# funkcijoje index nurodome, kad norėsime sugeneruoti index.html

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
