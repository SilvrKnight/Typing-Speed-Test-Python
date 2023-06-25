import time


def calculate_words_per_minute(words_typed, elapsed_time):
    minutes = elapsed_time / 60
    words_per_minute = words_typed / minutes
    return words_per_minute


def calculate_accuracy(text, user_input):
    correct_chars = sum([1 for i in range(len(text)) if text[i] == user_input[i]])
    total_chars = len(text)
    accuracy = (correct_chars / total_chars) * 100
    return accuracy


def run_speed_typing_test():
    print("Speed Typing Test")
    print("Type the following text. Press Enter when you're done.")
    print("Note: The timer will start as soon as you press Enter.\n")

    text = "The quick brown fox jumps over the lazy dog."
    print(text + "\n")

    input("Press Enter to start the timer...")
    start_time = time.time()

    user_input = input("> ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Count the number of words typed
    words_typed = len(user_input.split())

    # Calculate the words per minute
    words_per_minute = calculate_words_per_minute(words_typed, elapsed_time)

    # Calculate accuracy
    accuracy = calculate_accuracy(text, user_input)

    print(f"\nWords per minute: {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

    if accuracy < 100:
        print("Incorrect words:")
        for i in range(len(text)):
            if text[i] != user_input[i]:
                print(f"Position {i+1}: {text[i]} -> {user_input[i]}")


if __name__ == "__main__":
    run_speed_typing_test()
