import math

__author__ = 'Apollo'

class quadratic_solver:
    def demo(self):

        solve = 1

        while solve == 1:
            print("Enter coefficients 'a' 'b' and 'c' of a quadratic equation")
            a = int(input("coefficient a: "))
            b = int(input("coefficient b: "))
            c = int(input("coefficient c: "))
            d = b ** 2 - 4 * a * c

            if d >= 0:
                disc = math.sqrt(d)
                root1 = (-b + disc) / (2 * a)
                root2 = (-b - disc) / (2 * a)
                print(root1, root2)

            else:
                print('error: no real number roots found. ')

            solve = int(input('Enter \'1\' to continue, or \'0\' to exit. '))


quadratic_solver().demo()

