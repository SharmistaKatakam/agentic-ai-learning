memory = []

while True:

    user_input = input("Enter text (type exit to stop): ")

    if user_input.lower() == "exit":
        break

    memory.append(user_input)

    print("\nCurrent Memory:")

    for item in memory:
        print("-", item)

print("\nFinal Memory:")
print(memory)