
def isnamed(item):
    ''' Returns True if item.__name__ exists, otherwise False. '''
    # pylint: disable=W0104,W0702
    try:
        item.__name__
        return True
    except:
        return False

def dunder_check(string):
    ''' Check if the passed in string appears to be a dunder one ex: __a__. '''
    return string.startswith('__') or string.endswith('__')

def not_lambda(lam):
    '''
        "not" the results of calling the passed in lambda. Must take a single
        argument. Example:
        >>> seq = ['0.txt', '1.txt', 'abcd', 'abcd.txt']
        >>> my_lambda = lambda x: x.endswith('.txt')
        >>> list(filter(not_lambda(my_lambda), some_seq))
        ['abcd']
    '''
    return lambda x: not lam(x)
