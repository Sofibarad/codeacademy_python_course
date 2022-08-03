from app import db, Message

all_messages = Message.query.all()
# print(all_messages)

message_1 = Message.query.get(1)
# print(message_1.message)
message_antanas = Message.query.filter_by(name="Antanas")
print(message_antanas.all())

#  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]