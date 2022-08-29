# Per API (padavus JSON duomenis) leistų įvesti prekę į duomenų bazę (jos formavimui panaudoti sqlalchemy ORM).
# Prekė turi turėti id, pavadinimą, kainą ir kiekį
# Per API leistų peržiūrėti visas įvestas prekes
# Per API leistų peržiūrėti vieną konkrečią prekę
# Per API leistų pakoreguoti prekę
# Per API leistų ištrinti prekę
# Paleisti sukurta Flask API programą
# Sukurti kitą Python programą (API klientą), kuris jungtųsi prie anksčiau sukurti prekių API ir leistų per naršyklę pridėti prekes, jas peržiūrėti, paredaguoti, ištrinti ir t.t. Pati kliento programa neturi saugoti jokių duomenų (DB nereikalinga).


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'items_list.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    price = db.Column("price", db.Float)
    count = db.Column("count", db.Integer)

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'count')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class ItemResource(Resource):
    def get(self):
        return{'about': 'Hello world!'}

    def post(self):
        db.create_all()
        name = request.json['name']
        price = request.json['price']
        count = request.json['count']
        new_task = Item(name=name, price=price, count=count)
        db.session.add(new_task)
        db.session.commit()
        return ItemSchema.jsonify(new_task)

api.add_resource(ItemResource, '/')


if __name__ == '__main__':
    app.run(debug=True)