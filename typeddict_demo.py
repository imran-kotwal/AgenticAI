from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

p : Person = {'name' : 'jefe','age':32}

print(p)