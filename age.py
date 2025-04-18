age = int(input("Enter your age: "))
print()
print(f'You are {age} years old.')

for index in range(10, 41, 10):
    print(f'In {index} years, you will be {age + index} years old.')