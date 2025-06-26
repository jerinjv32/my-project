import csv
from collections import Counter
try:
    with open("products-100.csv", "r", newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        price = [] 
        category = []
        for row in reader:
            price.append(row[5])
            category.append(row[4])
        counter = Counter(category)
        most_common = counter.most_common(1)
        max_price = max(price)
        min_price = min(price)

        print(f"Max Price:{max_price}\nMin-price:{min_price}\nMost common item:{most_common}\n")

except Exception as e:
    print(e)