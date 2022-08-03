from app import Message, db

print(Message.query.all())

user = Message.query.filter_by(email = "jonas@gmail.com").first()
print(user.message)
user.email = "jonas@mail.com"
user.name = "Jonas1"
user.text = "Kazkoks labai rimtai atsilipimas?"

db.session.add(user)
db.session.commit()
print(Message.query.all())

antanas = Message.query.get(2)
antanas.email = 'geras.zmogus@lrs.lt'
db.session.add(antanas)
db.session.commit()
print(Message.query.all())

# [Jonas - jonas@mail.com, Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]

# [Jonas - jonas@mail.com, Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]
