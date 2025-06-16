def print_file(content):
    print(content)

def process_file(file_path, callback):
    try:
        with open(file_path, "r") as f:
            content = f.read()
            if not content:
                callback("[File is empty]")
            else:
                callback(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except Exception as e:
        print(f"Exception occured: {e}")

if __name__ == '__main__':
    process_file("myfile.txt", print_file)