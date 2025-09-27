# and - all conditions must be true
# or - at least one condition must be true
# not - reverse the result
#age = 25
'''
age = 20
is_student = True
print(age > 18 and is_student)  # True
print(age > 30 or is_student)   # True
print(not is_student)           # False#
'''
a = 10
b = 5
print(a > 5 and b < 1)  # False
print(a < 2 or b < 8)   # True
print(not (a == 5))       # True