def report(title, *values, **details):
    print("\n---", title, "---")

    if values:
        print("Values:")
        for v in values:
            print("-", v)

    if details:
        print("Details:")
        for key, value in details.items():
            print(f"{key}: {value}")

report(
    "Student Performance",
    85, 90, 78,
    name="Raj",
    grade="A",
    school="ABC School"
)

report(
    "Model Training",
    0.45, 0.32, 0.28,
    epochs=10,
    lr=0.01,
    optimizer="adam"
)

# Why is flexibility critical in real systems?
# When you build your Cafe App for Patna, you might hardcode things like currency="INR". Two months later, if you want to launch in Nepal:
# Rigid System: You have to rewrite the database, the payment function, and the UI to accept a new currency.
# Flexible System: You designed the payment function with **kwargs or a config object. You just pass currency="NPR" and the system adapts.
