a = [1, 2, 3, 4, 5]
b= [2,6,1,20,16]
#set conversion
s1=set(a)
s2=set(b)
s3 = s1.intersection(s2) #common values in both lists
print(list(s3))  # Output: [2, 1]