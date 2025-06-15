import random
number = random.randint(0,100)
tries = int(5)
while True:
    tries -= 1
    i_num = int(input("Choose a number in between 0 and 100"))
    if i_num == number:
        print(f"Your guess is right! {i_num} is the number!")
        break
    elif tries < 0:
        print(f"Oh no, the numeber was {number}")
        break
    else:
        print(f"Nope {i_num} is not the number")