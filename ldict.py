students = [
    {"name": "Hermionese", "house": "Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"jack Russel terrier"},
    {"name":"Draco", "house": "Slytherine", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")