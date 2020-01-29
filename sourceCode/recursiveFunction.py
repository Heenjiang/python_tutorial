#If a function calls itself internally, the function is recursive
#Write a recursive function that calculates factorials
#f(n!) = n*f((n-1)!)....
# def my_factorials(n):
#     if n <= 0:
#         raise TypeError('Numbers less than or equal to 0 have no factorial')
#     if n == 1:
#         return n
#     else:
#        return n * my_factorials(n-1)
# print(my_factorials(10))
#The calculation process is as follows:
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
#Using recursive functions requires care to prevent stack overflow. In a computer, function calls are implemented through a data structure
#called a stack. Whenever a function call is entered, the stack adds a layer of stack frames, and whenever the function returns, the stack
#subtracts one layer of stack frames. Since the size of the stack is not infinite, too many recursive calls will cause a stack overflow

#Hanoi Tower

# def honoi_tower(n, a, b, c):
#     if n == 1:
#         print('%s-->%s' %(a,c))
#     else:
#         honoi_tower(n-1, a, c, b)
#         print('%s-->%s' %(a,c))
#         honoi_tower(n-1, b, a, c)
# honoi_tower(3, 'a', 'b', 'c')