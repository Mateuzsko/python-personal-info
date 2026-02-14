name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your county: ")

print("\n--- Personal information ---")
print("Name:", name)
print("Age:", age)
print("Country:", country)

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Status: adult")
    else:
        print("Status: Under 18")
else:
    print("Age must be a number.")

input("\nPress Enter to exit.")
