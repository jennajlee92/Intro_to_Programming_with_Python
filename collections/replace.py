info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

new_list = []

for char in list(info):
    if char == ':':
        new_list.append('+')
    else:
        new_list.append(char)

print(''.join(new_list))

# From this chapter

info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'

# From Python documentation

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str, my_list, my_tuple, my_range)))