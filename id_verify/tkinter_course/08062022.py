# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# print(f"Dalyba: {a} / {b} = {padalinom}")

# import logging

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# logging.warning(f"Dalyba: {a} / {b} = {padalinom}")

# import logging

# logging.basicConfig(level=logging.DEBUG)

# # def dalyba(a, b):
# #     return a / b

# # a = 10
# # b = 5

# # padalinom = dalyba(a, b)

# # logging.debug(f"Dalyba: {a} / {b} = {padalinom}")

# import logging

# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG)

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5
# padalinom = dalyba(a, b)

# logging.debug(f"Dalyba: {a} / {b} = {padalinom}")

import logging

logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def dalyba(a, b):
    return a / b

a = 10
b = 5

padalinom = dalyba(a, b)
logging.debug(f"Dalyba: {a} / {b} = {padalinom}")