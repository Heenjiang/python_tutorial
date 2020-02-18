'''
If you've heard of TDD: Test-Driven Test Development, you should familar with
unit testing.
Unit testing is used to test the correctness of a module, a function, or a class
If the unit test passes, it means that the function we tested works properly.
If the unit test fails, either the function is buggy or the test conditions are
entered incorrectly. In short, a fix is needed to make the unit test pass
'''

'''
What's the point of passing a unit test?
If we make any changes to a function code, we only need to run the unit test again
If it passes, it means our modifications will not affect the original behavior
of the function
If the test fails, our modification is inconsistent with the original behavior.
Either modify the code or the test case
'''

'''
The biggest benefit of this test-driven-development model is to ensure that the
behavior of a program module conforms to the test cases we designed.
When it is modified in the future, it can greatly guarantee that the module's
behavior is still correct
'''

#Let's write a 'Dict' class. The behavior of this class is the same as 'dict'
#But it can be accessed through atrributes
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
#In order to write unit tests, we need to introduce the unittest module that
#comes with Python
import unittest

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
         d = Dict(a=1, b='test')
         self.assertEqual(d.a, 1)
         self.assertEqual(d.b, 'test')
         self.assertTrue(isinstance(d, dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
        
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# if __name__ == '__main__':
#     unittest.main()

'''
setup() And tearDown()
You can write two special setUp() and tearDown() methods in unit test class. 
These two methods are executed before and after each test method is called
What's the use of setUp() and tearDown() methods?
Imagine that your test needs to start a database. At this time, you can connect 
to the database in the setUp() method, and close the database connection in the
teatDown() method, so that you don't have to repeat the same code in each test
method
:
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
'''
