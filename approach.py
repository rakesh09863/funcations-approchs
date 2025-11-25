#define function for adding of two numbers
#apporoach1
print('i am for before function')
def sumop(k,v):# here k ad v are formal parameters
    r=k+v
    return r
print('main program')
res=sumop(10,11)#funcation call
print('sum={}'.format(res))
res=sumop(33,22)
print('sum={}'.format(res))