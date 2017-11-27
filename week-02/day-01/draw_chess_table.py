# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
for i in range(8):
    if i % 2 == 0:
        a = "%"
        b = " "
    else:
        a = " "
        b = "%"
    for j in range(4):
        print(a+b, end="")
    print()
