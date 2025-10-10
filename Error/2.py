try:
    file = open('C:\\python\\Error\\1.py', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    file.close()
    print("File closed.")