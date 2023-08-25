from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language = [python, ruby, visual_basic]
    print("The dynamically typed language are: ")
    for language in language:
        if language.is_dynamic():
            print(language.name)


main()
