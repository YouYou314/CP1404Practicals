def main():
    user_input = input("Enter a string: ")
    words = user_input.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_word_length = max(len(word) for word in word_counts)

# Print the word counts with aligned columns
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


if __name__ == "__main__":
    main()
