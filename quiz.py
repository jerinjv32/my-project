import csv
import sys

class QuizFile:
    question_list = {}

    def __init__(self, name):
        self.name = name

    def read(self):
        try:
            with open(self.name, newline="") as file:
                line = csv.DictReader(file)
                for row in line:  # This is an iterator is why row is used
                    self.question_list[row["index"]] = {
                        "quiz": row["quiz"],
                        "answer": row["answer"],
                    }
        except Exception as FileNotFoundError:
            print("The file is not found")
            sys.exit()

    def mark(self):
        for key in self.question_list.keys():
            q = self.question_list.get(key, {}).get("quiz")
            print(f"{key}, {q}")
            print(self.question_list.get(key, {}).get("answer"))
            mark = input("Enter the marks:")
            self.question_list[key]["mark"] = mark
        self.write_to_file()
    
    def write_to_file(self):
        fieldnames = ["index", "quiz", "answer", "mark"]
        with open(self.name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            for key, value in self.question_list.items():
                writer.writerow({
                    "index": key,
                    "quiz": value["quiz"],
                    "answer": value["answer"],
                    "mark": value["mark"]
                })

    def view_mark(self):
        total_marks = int(0)
        for key in self.question_list.keys():
            mark = self.question_list.get(key, {}).get("mark")
            total_marks += int(mark)
        print(f"Total Marks scored:{total_marks}")
    
    def check_file(self):
        if not self.question_list:
            return "1"
        else:
            return "0"

if __name__ == "__main__":
    name = input("Enter the name of the file with the format:")
    quiz_file = QuizFile(name)
    quiz_file.read()
    check = quiz_file.check_file()
    if check == "0":
        quiz_file.mark()
        quiz_file.view_mark()
    else:
        print(f"The file '{name}' is empty")
