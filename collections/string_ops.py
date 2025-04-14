print("what's up?".capitalize())        # What's up?
print('456ABC'.capitalize())            # 456abc

print("four SCORE and sEvEn".title())
# Four Score And Seven

print("i can't believe it's already mid-july.".title())
# I Can'T Believe It'S Already Mid-July. - Uses whitespace & punctuation as word boundaries

import string
print(string.capwords("i can't believe it's already mid-july."))
# I Can't Believe It's Already Mid-july. - Only breaks at whitespace

print("What's up?".swapcase())          # wHAT'S UP?
print('456ABC'.swapcase())              # 456abc
print('456ABC'.swapcase().swapcase())   # 456ABC

'Hello'.isalpha()      # True
'Good-bye'.isalpha()   # False: `-` is not a letter
'Four score'.isalpha() # False: space is not a letter
''.isalpha()           # False

'12340'.isdigit()      # True
'123.4'.isdigit()      # False: `.` is not a digit
'-1234'.isdigit()      # False: `-` is not a digit
''.isdigit()           # False

str.isalnum() #returns True if str is all letters and/or digits, False otherwise or if empty

str.islower() #returns True if all lowercase, False otherwise or if empty

str.isupper() #reverse of .islower()

str.isspace() returns True if all characters in str are whitespace characters, False otherwise. It returns False if the string is empty. The whitespace characters include ordinary spaces (), tabs (\t), newlines (\n), and carriage returns (\r). It also includes two rarely used characters: vertical tabs (\v) and form feeds (\f), as well as some foreign characters that count as whitespace.

Be careful with these methods: they're all Unicode-aware. Thus, 'Καλωσήρθες'.isalpha() returns True since the characters are all part of the Greek alphabet. If you need to exclude non-ASCII characters, use this pattern:

text.isalpha() and text.isascii()

'Four score and seven'.startswith('Four score')  # True
'Four score and seven'.startswith('For score')   # False
'Four score and seven'.startswith('score')       # False

'abc def'.startswith('def', 4)           # True
'abc def ghi'.startswith('def', 4, 7)    # True

'Four score and seven'.endswith('and seven')  # True
'Four score and seven'.endswith('ad seven')   # False
'Four score and seven'.endswith('score')      # False

'abc def'.endswith(('abc', 'xyz', 'stu'))  # False
'abc def'.endswith(('xyz', 'def'))         # True
'abc def'.endswith('def', 4)               # True
'abc def ghi'.endswith('def', 4, 7)        # True

text = '  Four     score and   seven years ago.   '
print(text.split())
# ['Four', 'score', 'and', 'seven', 'years', 'ago.']

print('no-spaces'.split()) # ['no-spaces']

text = ',Four,score,and,,,seven,years,ago,'
print(text.split(','))
# Pretty printed for clarity
# [
#     '',
#     'Four',
#     'score',
#     'and',
#     '',
#     '',
#     'seven',
#     'years',
#     'ago',
#     ''
# ]

# Character splitting done with list or tuple in Python

text = 'abcde'
print(list(text))             # ['a', 'b', 'c', 'd', 'e']
print(tuple(text))            # ('a', 'b', 'c', 'd', 'e')

text = '''
You were lucky to have a room. We used to have to
live in a corridor.
Oh we used to dream of livin' in a corridor!
Woulda' been a palace to us. We used to live in an
old water tank on a rubbish tip. We got woken up
every morning by having a load of rotting fish
dumped all over us.
'''

print(text.strip().splitlines())
# Pretty printed for clarity
[
    "You were lucky to have a room. We used to have to",
    "live in a corridor.",
    "Oh we used to dream of livin' in a corridor!",
    "Woulda' been a palace to us. We used to live in an",
    "old water tank on a rubbish tip. We got woken up",
    "every morning by having a load of rotting fish",
    "dumped all over us."
]

words = ['You', 'were', 'lucky']
print(''.join(words))         # Youwerelucky
print(' '.join(words))        # You were lucky
print(','.join(words))        # You,were,lucky
print('\n  '.join(words))
# You
#   were
#   lucky

school = 'launch school'

print(school.find(' '))       # 6
print(school.find('l'))       # 0
print(school.find('h'))       # 5
print(school.find('hoo'))     # 9
print(school.find('x'))       # -1 #not found
print(school.find('N'))       # -1 #not found

#searching from the reverse
print(school.rfind(' '))      # 6
print(school.rfind('l'))      # 12
print(school.rfind('h'))      # 9
print(school.rfind('hoo'))    # 9
print(school.rfind('oh'))     # -1 #not found
print(school.rfind('N'))      # -1 #not found

text = 'abc abc def abc' # .find(string, indexstart, indexend)

print(text.find(' ', 4))         # 7
print(text.find(' ', 8))         # 11

print(text.find('c', 0, 2))      # -1
print(text.rfind('c', 3, 10))    # 6