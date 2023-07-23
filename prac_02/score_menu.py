Menu = input("(G)et a valid score"
             "(P)rint result"
             "(S)how stars"
             "(Q)uit")


def main():
    print(Menu)
    choice = Menu
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid input error message")
        print(Menu)
        choice = Menu


def get_valid_score():
    score = float(input("Enter score: "))
    return score


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    stars = int(score)
    print("*" * stars)


main()
