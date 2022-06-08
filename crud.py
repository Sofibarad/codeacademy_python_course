from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projektas import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()
projektas1 = Projektas("Naujas pr.", 20000)
session.add(projektas1)
session.commit()

projektas2 = Projektas("2 projektas", 55000)
session.add(projektas2)
session.commit()
projektas1 = session.query(Projektas).get(1)

print(projektas1.name)
# Naujas pr.
projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
projektai = session.query(Projektas).all()

for projektas in projektai:
    print(projektas.name, projektas.price)
# Naujas pr. 20000.0
# 2 projektas 55000.0