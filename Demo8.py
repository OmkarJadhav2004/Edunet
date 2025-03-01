#identity Operators

x = 'a'
y = 'b'

print("x is y : ",x is y)
print("x is not y : ",x is not y)

print(f"x is y(return true if both are equal) : {x is y}")
print("---------------------------------")
x = ['a','b']
y = x
z = ['c','d']
print("x is y : ",x is y)
print("x is not y : ",x is not y)
print("x is z : ",x is z)

