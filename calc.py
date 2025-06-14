first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))

while True:
    choice = input("Choose an operation \n +:Addition \n -:Subtraction \n *:multiplication \n /:division \n ^.Exit \n")

    match choice:
        case '+':
            ans = first + second
            print(f"Sum of {first}+{second} is {ans}\n")
        case '-':
            ans = first - second
            print(f"Subtraction of {first}-{second} is {ans}\n")
        case '*':
            ans = first * second
            print(f"Product of {first}*{second} is {ans}\n")
        case '/':
            ans = first / second
            print(f"division of {first}/{second} is {ans}\n")
        case '^':            
            break
        case _:
            print("Wrong choice\n")