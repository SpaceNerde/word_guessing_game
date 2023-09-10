import random

word_list = [
    "weltraum",
    "erde",
    "jupiter",
    "mars",
    "venus",
]

def pick_random_word():
    range_ = len(word_list)
    word = word_list[random.randrange(range_)]

    return ",".join(word).split(",")

def player_guess(word_to_guess, word_progress):
    print("Try to guess a letter")
    player_input = input(">> ").lower()

    if player_input in word_to_guess:
        pos = [x for x in range(len(word_to_guess)) if word_to_guess[x]==player_input]
        for item_ in pos:
            print()
            word_progress.pop(item_)
            word_progress.insert(item_, player_input)
            print(word_progress)
    else:
        print("Letter not inside list")

if __name__ == "__main__":
    print("Space's Word Guessing Game")
    print()
    print("Guess the word")
    random_word = pick_random_word()
    word_progress = []
    for item in random_word:
        word_progress.append(item.replace(item, "_"))
    for item in word_progress:
        print(item)

    while random_word != word_progress:
        player_guess(random_word, word_progress)

    print("YOU WON!!!")