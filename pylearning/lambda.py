people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

#sort by people's names
# def f(person):
#     return person["name"]


people.sort(key=lambda person: person["name"])

print(people)