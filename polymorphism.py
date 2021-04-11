class Poly():

    def get_square(self, a=0, b=0):
        print('a = {}, b = {}'.format(a, b))
        if a != 0 and b != 0:
            print((a*b))
        elif a != 0 and b == 0:
            print((a**2))
        else:
            print('invalid input')


# poly = Poly()
# poly.get_square(a=2)
# poly.get_square(a=2, b =4)
# poly.get_square()
