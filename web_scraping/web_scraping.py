# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# # print(source)

# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')
# print(blokas.prettify())
# print("======")
# blokas = soup.find('h3', class_ = 'headline-title')
# print(blokas)

# blokas = blokas.find()
# print(blokas.prettify())

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')

# kategorija = blokas.find('div', class_ = 'headline-category').text.strip()

# tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
# print(kategorija)
# print(tekstas)

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')

# for blokas in blokai:
#     try:
#         kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#         tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#         print(kategorija)
#         print(tekstas)
#     except:
#         pass

# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')

# with open("delfi naujienos.csv", "w", encoding="UTF-8", newline='') as failas:

#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Kategorija', 'Tekstas'])
#     for blokas in blokai:
#         try:
#             kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#             tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#             csv_writer.writerow([kategorija, tekstas])
#         except:
#             pass

# import csv

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://shop.telia.lt/telefonai/?filter=brand:samsung').text
# soup = BeautifulSoup(source, 'html.parser')

# blokai = soup.find_all('div', class_ = 'card card__product card--anim js-product-compare-product')

# with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

#     for blokas in blokai:
#         try:
#             pavadinimas = blokas.find('a', class_ = 'card__title js-product-name-truncate').text.strip()
#             men_kaina = blokas.find('div', class_ = 'pull-left').span.text.strip()
#             kaina = blokas.find('span', class_ = 'price--marker').next_element.next_element.next_element.next_element.span.text.strip()
#             csv_writer.writerow([pavadinimas, men_kaina, kaina])
#         except:
#             pass

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/news/daily/world/karas-ukrainoje-rusu-ziniasklaida-ukrainoje-suciuptiems-britams-ir-marokieciui-mirties-bausme.d?id=90439595')
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('p')
# print(blokai[:8])

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai?filter=brand:samsung').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class = 'card card__product card--anim js-product-compare-product')
for blokas in blokai:
     # print(blokas.text.strip().replace("\n",""))
    name = blokas.find("a", class_ = "mobiles-product-card__title js-open-product").text.strip()
    print(name)
# blokas = soup.find('div', class_ = 'headline')
# print(blokas.prettify())

with open("Telia Samsung telefonai.csv", "w", encoding = "UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csw_writer.writerow(['Modelis, 'Mėnesio kaina', "Kaina"])

    for blokas in blokai:
        try:
            name = blokas.find("a", class = "mobiles-product-carf__title js-product-compare-product").text.strip()
            monthly_price = blokas.find("div", class_="mobiles-product-card__price-marker").text.strip()
            price = blokas.find("div", class_ ="mobiles-product-card__full-price price") \
            .find("div", class_="mobiles-product-card__price-marker").text.strip()
            csv_write.writerow([name, monthly_price, price])
        except:
            pass

