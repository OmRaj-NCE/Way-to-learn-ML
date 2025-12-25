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
