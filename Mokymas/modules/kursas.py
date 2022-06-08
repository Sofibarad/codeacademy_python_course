class Kursas:
    def __init__(self, pavadinimas: str, destytojas: str, trukme: int):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = trukme

    def destyti(self):
        print("Vyksta mokymas!")
