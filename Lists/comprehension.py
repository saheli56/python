"""
expression for item in iterable if condition
e - x * 2
item -
iterable - range(1,11)
condition optional
"""
squares = []
for x in range(1, 11):
    squares.append(x**2)
    print(squares)
squares2 = [x**2 for x in range(1, 20)]
print(squares2)
squares3 = [x**2 for x in range(1, 20) if x % 2 == 0] #even numbers
print(squares3)