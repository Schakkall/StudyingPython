import os

def clear():
    os.system("cls")


class Person:
    __code = 0
    __name = None
    __birth = 0
    __email = None
    __phone = None

    def __init__(self, code, name, birth, email, phone):
        self.__code = code
        self.__name = name
        self.__birth = birth
        self.__email = email
        self.__phone = phone

    def presents(self):
        print("Hello , my name is %s , I was born in %s , my email is %s and my phone number is %s"% \
              (self.__name, self.__birth, self.__email, self.__phone))



clear()
print("Hello World! Welcome to my Git testing!")
p = Person(0, "Jose", "15/06/1993", "somemail@gmail.com", "99900-0000")
p.presents()
Person.presents(p)


