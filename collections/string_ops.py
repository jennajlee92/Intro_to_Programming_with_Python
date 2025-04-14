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

