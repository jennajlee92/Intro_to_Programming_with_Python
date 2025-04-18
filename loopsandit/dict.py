my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { key: len(key) for key in my_set if len(key) % 2 != 0 }
print(result)