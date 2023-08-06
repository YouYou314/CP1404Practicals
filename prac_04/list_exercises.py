# Task 1:

def main():
    number = []

    for i in range(5):
        number = int(input("Number: "))
        number.append(number)

    print("The first number is", number[0])
    print("The last number is", number[-1])
    print("The smallest number is", min(number))
    print("The largest number is", max(number))
    print("The average of the number is", sum(number) / len(number))


main()
