# Sukurti funkcijas, kurios:

# Gražintų visų paduotų skaičių sumą (su *args argumentu)
# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
# Gražintų paduoto sakinio simbolių kiekį (su len())
# Gražintų rezultatą, skaičių x padalinus iš y
# Nustatyti standartinį logerį (logging) taip, kad jis:

# Saugotų pranešimus į norimą failą
# Saugotų INFO lygio žinutes
# Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
# Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:

# logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
# Paleisti kiekvieną funkciją su norimais argumentais


import math

def sum(*args):
    total = 0
    for x in args:
        total += x
    return total

sum(2,5,6)

def square_root(x: float) -> float:
    answer = math.sqrt(x)
    return answer

print (square_root(9))

def len_of_sentence(x):
    answer = len(x)
    return answer

print(len_of_sentence("Hey There"))

# def divide(x: int, y:int) -> int:
#     return x/y

import logging

# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG)
logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def sum(*args):
    total = 0
    for x in args:
        total += x
        logging.debug(f"suma: {total}")
    return total

sum(2,5,6)
