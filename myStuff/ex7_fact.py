def fact(fact1):
    fact2=fact1
    while ( fact1 > 1):
        fact2=fact2 * (fact1 - 1)
        fact1-= 1

    print ( "factorial is ", fact2)

f1 = raw_input ("what factorial do you need ? ")
fact(int(f1))
