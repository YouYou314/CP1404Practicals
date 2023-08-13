def main():
    user_input = input("Enter a string: ")
    words = user_input.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


