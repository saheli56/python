age= int(input('enter your age: '))
if age>= 18:
    print('you are eligible to vote')
elif age<=0:
    print('invalid age')
else:
    print('you are not eligible to vote')