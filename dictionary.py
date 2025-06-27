school = {
    "2023A001": {"name": "Alice", "class": "10", "section": "A"},
    "2023A002": {"name": "Bob", "class": "10", "section": "B"}
}

# for x, name in school.items():
#     print(f"Admission no: {x}")
#     for key, value in name.items():
#         print(f"{key}:{value}")
for key, value in school.items():
    print(f"Admission no:{key}")
    print(f"name:{value["name"]}")
    print(f"class:{value["class"]}")
    print(f"section:{value["section"]}")
# from csv import DictReader
# contact_list = {}
# with open("contact_list.csv", newline = "") as file:
#     contact = DictReader(file)
#     for row in contact:
#         contact_list[row['name']] = {
#             'phone_no' : row['phone_no'],
#             'address' : row['address']
#         }

# for key1, value1 in contact_list.items():
#     print(f"Name: {key1}\n")
#     for key2, value2 in value1.items(): 
#         print(f"{key2}\n{value2}")
    