#this method is used to change a perticular value in the list without affecting the original list
list1 = [1, 2, 3]
list2=list1.copy()
list2[0]=100
print(list1,list2)