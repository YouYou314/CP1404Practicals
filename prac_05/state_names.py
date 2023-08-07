"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    upper_state_code = state_code.upper()  # Convert user input to uppercase
    if upper_state_code in CODE_TO_NAME:
        print(upper_state_code, "is", CODE_TO_NAME[upper_state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:<4} is {state_name}")

