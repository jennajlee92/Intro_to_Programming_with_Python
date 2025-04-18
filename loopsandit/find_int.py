my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

result = []
def find_integers(tup):
    return [ item
             for item in tup
             if type(item) is int ]

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]