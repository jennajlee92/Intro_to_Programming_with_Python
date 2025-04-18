my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for number in my_list:
    if number % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

# Using a helper function with a ternary expression and list comprehension

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
           for number in my_list ]
print(result)