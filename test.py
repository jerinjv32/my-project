try:
    with open("myfile.txt", "r+") as file:
        line = file.readlines()
        print(line)
        line.pop(5)
        print(line)
        line = line.strip(',')
        file.write(line)
except Exception as e:
    print(f"[Exception Occured: {e}]")