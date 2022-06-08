# 1 užduotis
# Python faile padaryti šiuos veiksmus (atskirai, ne iškart):

# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką (.now().time()).
# Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
# Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.

from datetime import datetime , datetime as data

# print (datetime.now())
# print (type (date.today()))

print(data.today())

print(data.today().time())



