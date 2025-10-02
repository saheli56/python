list = [1, 2, 3, 4, 5]
print(list[2])
list[2] = "hello"
print(list)

#for updating multiple values slice assignment is used
list[1:4] = ["a", "b", "c"]
print(list)