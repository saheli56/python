with open('C:\\python\\File Handling\\data.txt', 'w') as file:
    content = input("Enter text to write to the file: ")
    file.write(content)
    print("Data written to file successfully.")