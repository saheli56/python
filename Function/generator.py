def count_down(num):
    while num > 0:
        yield num #yield pauses the function and returns a value
        num -= 1
for no in count_down(5):
    print(no)