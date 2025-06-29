from csv import DictReader, DictWriter
from sys import exit


class ReadFile:
    def __init__(self, file_name):
        self.__expense_box = {}
        self.__file_name = file_name
        try:
            with open(self.__file_name, newline="") as file:
                csv_line = DictReader(file)
                for row in csv_line:
                    self.__expense_box[row["index"]] = {
                        "item": row["item"],
                        "expense": row["expense"],
                    }
        except Exception as FileNotFoundError:
            exit("File Not Found")
        except Exception as e:
            print(f"[Exception: {e}]")

    @property
    def expense_box(self):
        return self.__expense_box

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, new_file_name):
        if not new_file_name:
            raise ValueError("File name can't be empty")
        else:
            self.__file_name = new_file_name


class LogExpense:
    def __init__(self, obj_r, item, expense=0):
        self.file_name = obj_r.file_name
        self.expense_box = obj_r.expense_box
        self.__item = item
        self.__expense = expense

    @property
    def expense(self):
        return self.__expense

    @expense.setter
    def expense(self, new_expense):
        if new_expense >= 0:
            self.__expense = new_expense
        else:
            print("Expense can't be null")

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, new_item):
        if not new_item:
            raise ValueError("Can't be empty")
        else:
            self.__item = new_item

    # Reading contents to dictionary
    def read_to_dict(self):
        self.expense_box[len(self.expense_box) + 1] = {
            "item": self.__item,
            "expense": self.__expense,
        }

    # Reading contents to file
    def read_to_file(self):
        try:
            with open(self.file_name, "w", newline="") as file:
                writer = DictWriter(file, fieldnames=["index", "item", "expense"])

                writer.writeheader()
                for key, value in self.expense_box.items():
                    writer.writerow(
                        {
                            "index": key,
                            "item": value["item"],
                            "expense": value["expense"],
                        }
                    )
        except Exception as e:
            print(f"Exception: {e}")


class Expense_calc:
    def __init__(self, obj_r):
        self.expense_box = obj_r.expense_box

    def calc_total(self):
        total = int(0)
        for value in self.expense_box.values():
            total += int(value["expense"])
        print(f"Total Expense: {total}")


if __name__ == "__main__":
    r = ReadFile("spending.csv")
    while True:
        option = input("1. Add \n2. Calculate\n^. Exit\nOption:")
        match option:
            case "1":
                item = input("Item name:")
                expense = input("Expense:")
                l = LogExpense(r, item, expense)
                l.read_to_dict()
                l.read_to_file()
            case "2":
                c = Expense_calc(r)
                c.calc_total()
            case "^":
                break
            case _:
                print("Wrong option")
