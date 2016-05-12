import os
from datetime import date


def clear():
    os.system("cls")


class Person:
    __code = 0
    __name = None
    __birth = None
    __email = None
    __phone = None

    def __init__(self, code):
        self.__code = code

    def __init__(self, code, name, birth, email, phone):
        self.__code = code
        self.__name = name
        self.__birth = birth
        self.__email = email
        self.__phone = phone

    def presents(self):
        print("Hello , my name is {name:s} , I was born in {birth:s} , my email is {mail:s} and my phone number is {pho\
ne:s}".format(name=self.__name, birth=self.__birth, mail=self.__email, phone=self.__phone))

    def tell_your_age(self):
        t = date.today()
        print("I'm {0:s}".format(str(t.year - int(self.__birth[6:]))))

    def test_variable_scope(self):
        a = 0

        def test2():
            b = 0
            a = 1
            print(a)

        test2()
        print(a)


clear()

print("\nHello World! Welcome to my Git testing!")

p = Person(0, "Jose", "15/06/1993", "somemail@gmail.com", "99900-0000")

p.presents()

Person.presents(p)
Person.tell_your_age(p)
# Person.test_variable_scope(p)
# Person.clear(p)
Person.presents(p)
# print(p.)

# print(p._Person__name)
# print(p.__name)
