def upper(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(upper('hello world'))
print(upper('goodbye'))