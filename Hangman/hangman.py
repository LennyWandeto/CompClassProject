import random  # Import the random module for random word selection

# List of possible words for the hangman game
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
    "short", "shine", "slice", "slope", "smile", "splash", "stain", "stark", "start", "steel", "stool", "straw",
    "swarm", "swirl", "tackle", "tapes", "theme", "thick", "throne", "toxin", "towel", "track", "train", "trend",
    "treat", "troop", "truth", "under", "unity", "upper", "usage", "vigor", "visit", "vowel", "wager", "waste",
    "water", "wave", "wheel", "whisk", "wrack", "wrist", "write", "zebra", "zenith", "zone", "zoom"]

def get_word():
    # Selects a random word from the word list and returns it in uppercase
    term = random.choice(word_list)
    return term.upper()

def play(term):
    # Initializes variables for the game
    word_completion = "_" * len(term)  # Placeholder for the word to guess
    guessed = False  # Indicates if the word is guessed
    guessed_letters = []  # List of guessed letters
    guessed_words = []  # List of guessed words
    tries = 0  # Number of tries allowed
    print("Let's test your word skills with a game of hangman!")
    print(display_hangman(tries))  # Show initial hangman
    print(word_completion)  # Show word completion with underscores
    print("\n")
    
    while not guessed and tries < 6:  # Continue until the word is guessed or tries run out
        guess = input("Please guess a letter or word:").upper()
        
        # Single letter guess
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in term:
                print(guess, "is not in the word.")
                tries += 1  # Deduct a try if incorrect
                guessed_letters.append(guess)  # Add to guessed letters
            else:
                print("Correct!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(term) if letter == guess]  # Find indices of correct letter
                for index in indices:
                    word_as_list[index] = guess  # Reveal letter in word_completion
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:  # All letters guessed
                    guessed = True

        # Full word guess
        elif len(guess) == len(term) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != term:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = term  # Complete the word if guessed correctly

        # Invalid guess
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))  # Display current hangman state
        print(word_completion)  # Display current word completion
        print("\n")
    
    # Game outcome messages
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. Better luck next time! The word was " + term)

def display_hangman(tries):
    # List of hangman stages for each incorrect guess count
    stages = [ 
        """
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
        /|\\  |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ------
        """
    ]
    return stages[tries]  # Return the current hangman stage based on tries left

def main():
    # Main game function
    term = get_word()  # Get a random word to start the game
    play(term)  # Start the game with the selected word
    while input("Play Again? (Y/N) ").upper() == "Y":  # Prompt to play again
        term = get_word()  # Get a new random word
        play(term)  # Start a new game round
if __name__ == '__main__':
    main()