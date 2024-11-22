from Pong.main import Pong

print("Welcome to Hectors Minigames!!")
print("Choose a game to play:")
print("1. Pong")
print("2. Hangman")
choice = input("Choose here: ")
if choice == "1":
    game = Pong()
    game.run()