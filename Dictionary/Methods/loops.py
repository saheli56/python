profile = {
    "name":"Alice","age":28,"skills":["Python","Data Analysis","Machine Learning"]
}

for key in profile:
    print(key)
    print(profile[key])
    for value in profile.values(): # for value
        print(value)
        
for item in profile.items(): # for item
        print(item)
        print(type(item)) # tuple