def say(text='hello'):
    """
    The say function prints 'hello!' as a default and 'text!' otherwise
    """
    print(text + '!')

print(say.__doc__)
say('Howdy')
say()