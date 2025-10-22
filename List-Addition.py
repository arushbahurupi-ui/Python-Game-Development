list1 =[[1, 2, 3],
        [4, 5, 6]]
list2 = [[7, 8, 9],
        [10, 11, 12]]

result = []

for r in range(len(list1)):
    row = []
    for c in range(len(list1[0])):
        row.append(list1[r][c] + list2[r][c])
    result.append(row)

print(result)


