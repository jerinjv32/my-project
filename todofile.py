def menu():
    file_path = "myfile.txt"
    while True:
        choice = input("\n\t\t===MENU===\n\t1).Add\n\t2).Check\n\t3).View\n\t^).Exit\nOption:")
        match choice:
            case '1':
                file_manage(file_path, "a", view)            
            case '2':
                file_manage(file_path, "r+", view)
            case '3':
                file_manage(file_path, "r", view)
            case '^':
                break
            case _:
                print("[Wrong Option]\n")

def view(contents):
    print(contents)

def file_manage(path, action, callback):
    try:
        with open(path, action) as file:
            match action:
                case 'r':
                    for line in file:
                        callback(line)
                case 'a':
                    content = input("New task: ")
                    save = input("Do you want to save?: Y)Yes N).No:")
                    if save in ['y','Y']:
                        content = "\n" + content
                        file.write(content)
                        print('Saved Successfully\n')
                    else:
                        callback('No Change\n')
                case 'r+':
                    line_no = int(input("Enter the line to be deleted:"))
                    content = file.readlines()
                    print(content)
    except FileNotFoundError:
        print(f"[File {path} not found]\n")
    except Exception as e:
        print(f"[Exception:{e} Occured]\n")

if __name__ == "__main__":
    menu()