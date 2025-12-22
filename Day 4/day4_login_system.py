# manually
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# improve it
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")


# How would this scale to 1,000 users?
# 1. The Data (This simulates your database)
# In a real app, this data would come from a file or database, not code.
user_database = {
    "admin": "1234",
    "john_doe": "securePass1",
    "alice_w": "alice123",
    # ... imagine 997 more users here ...
}
# 2. The Input
username = input("Enter username: ")
password = input("Enter password: ")
# 3. The Logic (Remains the same regardless of user count)
if username in user_database:
    # User exists, now check password
    if user_database[username] == password:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
