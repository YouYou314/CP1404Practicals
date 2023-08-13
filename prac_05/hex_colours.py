COLOR_TO_HEX = {
    "ALICEBLUE": "FOF8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2",
}


def lookup_color_code(color_name):
    return COLOR_TO_HEX.get(color_name.upper())


color_name = input("Enter a color name: ")

while color_name != "":
    color_code = lookup_color_code(color_name)
    if color_code:
        print(f"{color_name.upper()} color code is {color_code}")
    else:
        print("Invalid color name")

    color_name = input("Enter a color name: ")
