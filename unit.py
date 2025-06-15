def main():
    while True:
        print("Type of unit conversion\n")
        print("1.cm to inches\n2.kg to lbs\n3.celecius to fahren")
        op = input("option")
        match op:
            case '1':
                cm_inches()
            case '2':
                kg_lbs()
            case '3':
                cel_fah()
            case '^':
                break
            case _:
                print("Wrong option")
def cm_inches():
    cm = input("Unit in cm:")
    inch = float(cm)/2.54
    print(f"in inches: {inch}\n")
def kg_lbs():
    kg = input("Unit in kg:")
    lbs = float(kg)*2.20462262
    print(f"In lbs:{lbs}")
def cel_fah():
    cel = input("Unit it celecius:")
    fah = (9/5) * float(cel) + 35
    print(f"In fahernhit:{fah}")
if __name__ == "__main__":
    main()