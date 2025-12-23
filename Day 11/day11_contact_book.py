contacts = {}

n = int(input("How many contacts? "))

for i in range(n):
    name = input(f"Enter name {i+1}: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

print("\n--- CONTACT BOOK ---")
for name, info in contacts.items():
    print(f"{name}: Phone={info['phone']}, Email={info['email']}")


#Ask yourself:
# Why do APIs return JSON (dictionaries)?
# How would I store ML model metadata?
# Why are nested dictionaries so powerful?


# Dictionaries are labeled: If I send you {"name": "Om", "age": 21, "grade": "A"}, you know exactly what "21" is.
# Resilience: I can add a new key, {"country": "India"}, later on, and your old code won't crash because it just ignores keys it doesn't recognize. This allows APIs to upgrade without breaking 1,000 users' apps. 

#model_config = {
#    "architecture": "Neural Network",
#    "created_at": "2025-12-23",
#    "hyperparameters": {
#        "learning_rate": 0.001,
#        "epochs": 50,
#        "batch_size": 32
#    },
#    "results": {
#        "accuracy": 94.5,
#        "loss": 0.05
#    }
#}
