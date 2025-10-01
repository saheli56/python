'''
slicing is a way to get a substring from a string.
string[start:end:step]
start: starting index (inclusive)
end: ending index (exclusive)
step: step size (optional)
'''
text = "Code never lies, comments sometimes do!"
print(text[1:5:1])
print(text[1:8:2]) #space between each character
print(text[::]) # entire string
print(text[::-1]) # reverse the string
print(text[:5]) # first 5 characters
