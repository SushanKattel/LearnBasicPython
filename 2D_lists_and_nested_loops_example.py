two_d_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(two_d_list[0][2])
print(two_d_list[2][2])
print("---------------------------------------------")

for row in two_d_list:    # you can write jpt in place of row
    print(row)
print("---------------------------------------------")

for row in two_d_list:
    for col in row:
        print(col)    # It gives individual elements... This is example of nested loop in 2D array.

