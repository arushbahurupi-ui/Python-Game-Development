
list2 = []

row = int(input("How many rows do you want: "))
column = int(input("How many columns do you want: "))

for d in range(row):
    list3 = []
    for f in range(column):
        number = int(input("What number do you want to add to your list?: "))
        list3.append(number)
    list2.append(list3)


for i in range(len(list2)):
    print(list2[i][i])
