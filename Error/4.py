def check_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    print("Password is valid.")
try:
    password = input("Enter your password: ")
    check_password(password)
except ValueError as e:
    print(f"Error: {e}")