
#  python -m pydoc raw_input
def add2(a,b):
    print("\aaddition is", int(a) + int(b) )
def sub2(a,b):
    print("substraction is", int(a) - int(b))


print "this is a calculator"
print"enter 2 numbers"
x=raw_input("enter x : ")
y=raw_input("enter y : ")
op=raw_input("enter opertation : ")
print ("you entered", op)
if  op == "add":
    add2(x,y)
elif op == "sub":
    sub2(x,y)
else:
    print "nonE"

z= int(x) +int (y)
print "result of ",x,op, y, "is :", z
