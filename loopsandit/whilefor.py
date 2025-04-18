my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    if number % 2 == 0:
        print(number)
    index += 1

print()

for number in my_list:
    if number % 2 == 1:
        print(number)

print()

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for number in list:
        if number % 2 == 0:
            print(number)