list1 =[[1, 2, 3],
        [4, 5, 6]]
list2 = [[7, 8, 9],
        [10, 11, 12]]

result =[[0, 0, 0],
        [0, 0, 0]]

for i in range(len(list1)):
    for j in range(len(list1[1])):
        result[i][j] = list1[i][j] + list2[i][j]

print(result)

