from unicodedata import name


my_variable = "This is my global variable"

print("my_model has bees successfully imported")


def write_backwards(sentence: str) -> str:
    print(sentence[::-1])
    
write_backwards("Hello")

class Person():
    def__init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def say_hello(self)
        print(f'Hi my name is {self.name}, Im {self.age}")