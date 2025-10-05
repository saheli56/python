profile = {
    'name':"Alice", 'age':28, 'skills':["Python","Data Analysis","Machine Learning"]
}
print(profile.values())
print(type(profile.values()))  # dict_values 
print(list(profile.values()))  # convert to list ['Alice', 28, ['Python', 'Data Analysis', 'Machine Learning']]
print(tuple(profile.values()))  # convert to tuple ('Alice', 28, ['Python', 'Data Analysis', 'Machine Learning'])