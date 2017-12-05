# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def div_ten_by(divisor):
    try:
        print(10 / divisor)
    except ZeroDivisionError:
        print("fail")

div_ten_by(3)
div_ten_by(0)