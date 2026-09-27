print("=" * 40)
print("       AKSHAYA'S SKILL EXPLORER")
print("=" * 40)

name = input("Hey there! What is your name? ")

print(f"\nWelcome, {name}!")
print("Let's explore my coding journey.\n")

skills = {
    "1": "Python - Learning to build useful programs",
    "2": "C - Practicing programming fundamentals",
    "3": "HTML & CSS - Exploring web development",
    "4": "Java - Currently learning object-oriented programming"
}

while True:
    print("\nChoose a skill to explore:")
    print("1. Python")
    print("2. C")
    print("3. HTML & CSS")
    print("4. Java")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice in skills:
        print("\n" + skills[choice])
    elif choice == "5":
        print(f"\nThanks for exploring, {name}!")
        print("Keep learning. Keep building!")
        break
    else:
        print("Please enter a valid choice from 1 to 5.")
