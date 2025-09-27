'''
is - true if both variables point to the same memory location
is not - true if both variables point to different memory locations
'''
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)      # True
print(a is c)      # False