import math
def main():
    bill_amt = int(input("Enter bill amount:"))
    tip_perc = int(input("Enter tip percentage:"))
    n = int(input("Enter the number of people splitting:"))
    if bill_amt > 0 and tip_perc > 0 and n > 0:
        tip(bill_amt, tip_perc, n)
    else:
        print("Negative value is not possible and people cant be zero")

def tip(bill_amt, tip_perc, n):
    tip = bill_amt * (tip_perc/100)
    math.floor(tip)
    final_bill = bill_amt + tip
    split = final_bill / n
    math.ceil(split)
    print(f"Tip:{tip}\nTotal bill amount:{final_bill}\nSplit:{split}")

if __name__ == "__main__":
    main()