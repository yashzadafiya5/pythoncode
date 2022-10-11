#inverted full peramid
number=5
fun=0
while number>=0:
    space=0
    while space<fun:
        print(" ",end="")
        space = space +1
    i=0
    while i <=number:
        print("* ",end="")
        i=i+1
    print("")
    number=number-1
    fun=fun+1