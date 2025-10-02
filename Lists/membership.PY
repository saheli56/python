"""
in - True/False
not in - opposite
"""
# case 1: in
lst = [1, 2, 3, 4, 5]
check = int(input("Enter a number to check: "))
if check in lst:
    print(f"{check} is present in the list")
else:
    print(f"{check} is not present in the list")
# case 2: not in
if check not in lst:
    print(f"{check} is not present in the list")
else:
    print(f"{check} is present in the list")