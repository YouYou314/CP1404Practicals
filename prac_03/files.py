# Step 1
name = input("Please enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

# Step 2
with open("name.txt", "r") as file:
    name = file.read()

print("Your name is", name)

# Step 3
with open("numbers.txt", "w") as file:
    file.write("17\n42\n400")

with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())

result = first_number + second_number
print("The result is:", result)

# Step 4
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number

print("The total is:", total)
