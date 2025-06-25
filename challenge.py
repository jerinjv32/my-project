data = ["apple", "banana", "apple", "orange", "banana", "apple"]

a_counter = int(0)
b_counter = int(0)
o_counter = int(0)
for n in data:
    if n == 'apple':
        a_counter += 1
    if n == 'banana':
        b_counter += 1
    if n == 'orange':
        o_counter += 1
    
if (a_counter > b_counter) and (a_counter > o_counter):
    print(f"Most frequent item: apple ({a_counter} times)")
elif (b_counter > o_counter):
    print(f"Most frequent item: banna ({b_counter} times)")
else:
    print(f"Most frequent item: orange ({o_counter} times)")