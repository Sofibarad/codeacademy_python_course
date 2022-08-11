from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
# from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField

import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite?check_same_thread=False')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

association_table = db.Table('association', db.metadata,
    db.Column('tevas_id', db.Integer, db.ForeignKey('tevas.id')),
    db.Column('vaikas_id', db.Integer, db.ForeignKey('vaikas.id'))
)

class Tevas(db.Model):
    __tablename__ = 'tevas'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    vaikai = db.relationship("Vaikas", secondary=association_table,
                          back_populates="tevai")

class Vaikas(db.Model):
    __tablename__ = 'vaikas'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    tevai = db.relationship("Tevas", secondary=association_table,
                         back_populates="vaikai")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tevai")
def parents():
    try:
        visi_tevai = Tevas.query.all()
    except:
        visi_tevai = []
        print("I broke down")
    return render_template("tevai.html", visi_tevai=visi_tevai)

                        
db.create_all()
