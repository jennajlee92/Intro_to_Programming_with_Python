'straße'.casefold() == 'strasse'.casefold()

"""
While casefold is only needed when working with non-US characters,
it's best practice in Python to use casefold instead of lower or upper,
especially when comparing strings.
"""