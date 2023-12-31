class ProgrammingLanguage:

    def __int__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, first appeared in {self.year} "

    def is_dynamic(self):
        return self.typing == "Dynamic"


def run_tests():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language = [python, ruby, visual_basic]
    print(python)

    print("The dynamically typed language are: ")
    for language in language:
        if language.is_dynamic():
            print(language.name)

    run_tests()
