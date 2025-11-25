#define function to add two numbers
#input:taken inside function body
#process:done in function body
#output:display in function body
def sumop():
    a=int(input('enter the a value:'))
    b=int(input('enter the b value:'))
    r=a+b
    print('sum({}+{})={}'.format(a,b,r))
#main program
sumop()