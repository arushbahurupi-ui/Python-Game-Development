list1 =  [[1,2],[3,4],[5,6]]


"""for i in list1:
    for j in i:
        print(j, end =" " )
    print()"""




"""for a in range(len(list1)):
    for b in range(len(list1[a])):
        print(list1[a][b], end = " ")
    print()"""


list2 = []

row = int(input("How many rows do you want: "))
column = int(input("How many columns do you want: "))

for d in range(row):
    list3 = []
    for f in range(column):
        number = int(input("What number do you want to add to your list?: "))
        list3.append(number)
    list2.append(list3)

print(list2)

