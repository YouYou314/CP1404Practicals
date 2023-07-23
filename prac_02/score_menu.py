import random
Menu = input("(G)et a valid score"
             "(P)rint result"
             "(S)how stars"
             "(Q)uit")


def main():
    print(Menu)
    score = float(input("Enter score: "))
    score = get_valid_score(score)
    choice = input("Your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            score = get_valid_score(score)
        elif choice == "P":
            result = get_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid input error message")
        print(Menu)
        choice = input("Your choice: ").upper()
    else:
        print("Farewell.")

    random_score = random.uniform(0, 100)
    result = get_score_result(random_score)
    print(f"Random Score: {random_score:.2f};\n{result}")


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def get_score_result(score):
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    stars = int(score)
    print("*" * stars)


main()
