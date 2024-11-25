import random


word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
             "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli",
             "vital", "watermelon", "yellowfruit", "zucchini", "abacus", "abandon", "abduct", "ability",
             "able", "absence", "absorb", "absurd", "accent", "accept", "access", "accident", "acclaim", "accord",
             "accuse", "achieve", "acquire", "address", "advance", "advice", "affect", "afford", "against", "agency",
             "alcohol", "allege", "alpine", "alter", "amazing", "ancient", "analyze", "animal", "annual", "answer",
             "anxiety", "applied", "approve", "around", "arrival", "arrive", "article", "artist", "aspect", "assault",
             "assert", "assess", "assure", "attain", "attempt", "average", "ballet", "battery", "bitter", "blanket",
             "bother", "bottle", "bottom", "bounce", "bracket", "bricks", "brides", "brother", "buckle", "buffer",
             "cabinet", "cattle", "chance", "change", "charge", "charms", "cherry", "choice", "choose", "church",
             "circle", "clutch", "courage", "coyote", "crater", "crisis", "crunch", "debate", "decade", "dental",
             "deploy", "design", "devote", "digest", "direct", "doubt", "douse", "drought", "duty", "echoes", "elbow",
             "enemy", "enrich", "enroll", "envoy", "escape", "escalate", "essay", "evoke", "exact", "examine", "expose",
             "extend", "extract", "facing", "famous", "fence", "final", "finish", "flame", "flour", "focus", "follow",
             "forbid", "force", "fortify", "found", "future", "gadget", "gather", "genuine", "giant", "global", "glove",
             "grasp", "grill", "group", "guilt", "gush", "habit", "hatch", "haunt", "hectic", "honey", "honor", "hover",
             "impact", "impose", "induce", "input", "invite", "island", "jacket", "juggle", "judge", "jumpy", "latch",
             "laugh", "leaf", "leap", "light", "liver", "lobby", "lunar", "luxury", "mango", "march", "merge", "mice",
             "model", "motor", "mouth", "music", "mutate", "mystic", "naive", "nurse", "number", "obtain", "occur",
             "olympic", "opera", "orbit", "order", "other", "outfit", "owner", "pace", "paint", "pause", "pencil",
             "pepper", "phase", "phone", "phrase", "place", "plaza", "point", "prize", "proof", "punch", "purse",
             "quote", "racket", "reach", "react", "reason", "rectify", "relax", "remedy", "repeat", "rescue", "result",
             "revise", "rider", "right", "robot", "sacred", "scout", "search", "sector", "shame", "sheet", "shock",
             "short", "shine", "slice", "slope", "smile", "splash", "stain", "stark", "start", "steel", "stool",
             "straw",
             "swarm", "swirl", "tackle", "tapes", "theme", "thick", "throne", "toxin", "towel", "track", "train",
             "trend",
             "treat", "troop", "truth", "under", "unity", "upper", "usage", "vigor", "visit", "vowel", "wager", "waste",
             "water", "wave", "wheel", "whisk", "wrack", "wrist", "write", "zebra", "zenith", "zone", "zoom"]


def get_word():
    term = random.choice(word_list)
    return term.upper()


def play(term):
    word_completion = "_" * len(term)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0
    print("Let's test your word skills with a game of hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries < 6:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in term:
                print(guess, "is not in the word.")
                tries += 1
                guessed_letters.append(guess)
            else:
                print("Correct!", guess, "is in the word!")
                guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(term) if letter == guess]
        for index in indices:
            word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
        if len(guess) == len(term) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != term:
                print(guess, "is not the word.")
                tries += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = term

        print(display_hangman(tries))
        print(word_completion)
        print('Guessed Letters:',guessed_letters)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry you ran out of tries, better luck next time! The word was" + " " + term)


def display_hangman(tries):
    stages = ["""
     -----
     |   |
         |
         |
         |
         |
    ------
    """,
              """
                -----
                |   |
                O   |
                    |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
                |   |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|   |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|\  |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|\  |
               /    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|\  |
               / \  |
                    |
               ------
               """]
    return stages[tries]


def hangman():
        term = get_word()
        play(term)
        if input("Play Again? Type 'Y' if you want to keep playing, if not press any other key you'd like to return to the main menu. ").upper() == "Y":
                gword = get_word()
                play(gword)







