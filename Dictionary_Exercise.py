dic = {"Jacket": 3.29, "Cap": 1.29, "Broom": 1.99}
bill = {}

for i,j in dic.items():
    print(i,"-", j, "€")

total = 0

while True:
    c = input("Type STOP to end. Enter an item: ")
    if c == "STOP":
        print("This is your final bill")
        for i, j in bill.items():
            cost = j * dic[i]
            print(i, "-", j, "x", dic[i], "€ =", cost, "€")
            total = total + cost
        print(f"\nYour total cost: {total:.2f} ")
        break
    elif c in dic.keys():
        quantity = input("In which quantity are you buying this item: ")
        bill[c] = float(quantity)