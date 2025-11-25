#input:inside in function body
#process:inside in function boby
#output:function call
def sumop():
    a=int(input('enter the a value:'))#inputs(30,56)
    b=int(input('enter the b value:'))
    c=a+b
    d=a-b
    x=int(input('enter the x value:'))#diferent inputs(10,20)
    y=int(input('enter the y value:'))
    z=x*y
    return a,b,c,d,x,y,z

#main program
k,v,r,s,x,y,z=sumop()#funcation call with multiline assignment
print('sum({}+{})={}'.format(k,v,r))
print('sub({}-{})={}'.format(k,v,s))
print('mul({}*{})={}'.format(x,y,z))
