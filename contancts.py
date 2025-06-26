import csv

contact_list = {}
file_path = "contact_list.csv"
try:
    with open(file_path, newline="") as file:
        contact = csv.DictReader(file)
        for row in contact:
            contact_list[row["phone_no"]] = {
                "name": row["name"],
                "address": row["address"],
            }
except Exception as e:
    print(f"[Exception 1:{e}]")


def menu():
    while True:
        choice = input("(1).Add\n(2).Delete\n(3).Search\n(^).Exit\nOption:")
        match choice:
            case "1":
                file_rw("add", view)
            case "2":
                file_rw("delete", view)
            case "3":
                file_rw("search", view)
            case "^":
                break
            case _:
                print("\nWrong option")


def view(lines, op):
    if op == "0":
        for number, contact in list.items():
            print(f"Phonw: {number}\n")
            for key, value in contact.items():
                print(f"{key}\n{value}")
    else:
        print(lines)


def file_rw(option, callback):
    try:
        fieldnames = ["index", "name", "phone_no", "address"]
        match option:
            case "add":
                name = input("Name:")
                number = input("Number:")
                address = input("Address:")
                if number in contact_list.keys():
                    callback("Number already exists\n", "1")
                else:
                    contact_list[number] = {"name": name, "address": address}
                    with open(file_path, "w", newline="") as file:
                        writer = csv.DictWriter(file, fieldnames)
                        writer.writeheader()
                        for i, (key, value) in enumerate(contact_list.items(), start=1):
                            writer.writerow(
                                {
                                    "index": i,
                                    "name": value["name"],
                                    "phone_no": key,
                                    "address": value["address"],
                                }
                            )
                    callback("Added to list", "1")
            case "delete":
                if not contact_list:
                    callback("No contacts is available", "1")
                else:
                    number = input("Enter the number to be deleted:")
                    if number in contact_list.keys():
                        noy = input(
                            f"Are you sure to delete the number:{number}? Y:yes N:no\nOption:"
                        )
                        if noy == "Y" or noy == "y":
                            del contact_list[number]
                            with open(file_path, "w", newline="") as file:
                                writer = csv.DictWriter(file, fieldnames)
                                writer.writeheader()
                                for i, (key, value) in enumerate(
                                    contact_list.items(), start=1
                                ):
                                    writer.writerow(
                                        {
                                            "index": i,
                                            "name": value["name"],
                                            "phone_no": key,
                                            "address": value["address"],
                                        }
                                    )
                                callback("Deleted Successfully", "1")
                        else:
                            callback("Deletion is cancelled", "1")
                    else:
                        callback("Number not found", "1")

            case "search":
                if not contact_list:
                    callback("No contacts is available", "1")
                else:
                    search = input("Enter the number:")
                    list = {}
                    if search in contact_list.keys():
                        list[search] = {
                            "name": contact_list.get(search, {}).get("name"),
                            "address": contact_list.get(search, {}).get("address"),
                        }
                        print("The number you have searched belongs to\n")
                        callback(list, 0)
                    else:
                        callback("Not available", "1")
    except Exception as e:
        print(f"[Exception 2:{e}]")


if __name__ == "__main__":
    menu()
