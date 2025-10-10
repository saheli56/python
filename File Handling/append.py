with open('C:\\python\\File Handling\\data.txt', 'a') as file:
    content = input("Enter text to append to the file: ")
    file.write(content)
    print("Data appended to file successfully.")