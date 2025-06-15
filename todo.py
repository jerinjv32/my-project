do_list = []
def main():
    while True:
        print("\nChoose an Option given below:")
        print("1).Add")
        print("2).Remove")
        print("3).View")
        print("^).Exit")
        choice = input("Option:")
        match choice:
            case '1':
                programs = input("Enter the number of programs:")
                addList(programs)
            case '2':
                k = int(input("Enter the program id to be removed:"))
                removeProg(k)
            case '3':
                view()
            case '^':
                break
            case _:
                print("Option doesn't exists\n")

def addList(k):
    do_num = int(0)
    for i in range(1,int(k)+1):
        do_num += 1
        do_list.insert(i ,input(f"{do_num}."))

def removeProg(k):
    if do_list:
        if len(do_list) > k and k > 0:
            do_list.pop(k)
            print(f"{k}th item is removed\n")
    else:
        print("No items are added yet\n")

def view():
    if do_list:
        for i in range(0, len(do_list)):
            print(f"{i+1}.{do_list[i]}")
    else:
        print("No items are added yet\n")

if __name__ == "__main__":
    main()