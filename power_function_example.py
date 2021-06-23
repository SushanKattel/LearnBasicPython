def power_function(base, pow_num):
    result = 1
    for jpt in range(pow_num):
        result = result * base
    return result

# x = int(input("Enter the base number: "))
# y = int(input("Raise to power?: "))

# print(int(power_function(x, y)))
# or you can write as follows also....
print(int(power_function(int(input("Enter the base number: ")), int(input("Raise to power?: ")) )))

