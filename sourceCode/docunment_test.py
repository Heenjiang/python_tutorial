'''
If you often read Python's official documentation, you can see many modules have sample code. For example,
the 're' module comes with a lot of sample code.
These example codes can be entered and executed in the interactive enviroment in Python, and the results
are consistent with the example code shown in the docunmentation
These code and other instructions can be written in comments, and then some tools can automatically
generate documentation, since these codes can be run directly, is it possiable to automatically execute
the code that written in the comments?
YES!
Python's built-in 'doctest' module can directly extract code from comments and execute it
The 'doctest' module strictly follows the input and output of the  Python interactive command line
to determine whether the test  results are correct
'''

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()