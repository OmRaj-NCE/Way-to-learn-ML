import numpy as np

data = []

# n = int(input("How many records? "))
# for i in range(n):
#     x = int(input("Feature 1: "))
#     y = int(input("Feature 2: "))
#     data.append([x, y])
n = int(input("How many records? "))
i = 0
while i < n:
    try:
        print(f"\n--- Entering Record {i+1} ---")
        x = int(input(f"Feature 1: "))
        y = int(input(f"Feature 2: "))
        data.append([x, y])
        i += 1  # Only move to the next record if input was successful
    except ValueError:
        print(">> Error: Please enter a valid number.")
    except KeyboardInterrupt:
        print("\n>> Program paused. Please type your numbers and press Enter.")
        # This catch helps prevent the script from closing on accidental clicks

arr = np.array(data)

print("\nDataset:\n", arr)

mean = arr.mean(axis=0)
std = arr.std(axis=0)

standardized = (arr - mean) / std

print("\nMean:", mean)
print("Std:", std)

print("\nStandardized data:\n", standardized)

# check distribution
print("\nNew mean:", standardized.mean(axis=0))
print("New std:", standardized.std(axis=0))
