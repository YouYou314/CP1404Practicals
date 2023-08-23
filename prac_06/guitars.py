from prac_06.guitar import Guitar


def main():
    guitar = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_add = Guitar(name, year, cost)
        guitar.append(guitar_add)
        print(guitar_add, "added.")
        name = input("Name: ")

    guitar.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar.append(Guitar("Line 6 JTV-59", 2010, 1512.9))