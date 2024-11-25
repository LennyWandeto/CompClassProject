from Minigames.Pong.pong import Game
from Minigames.hangman.Hangman import hangman
from Minigames.BeeGame.code.platformmain import Platform



def main_menu():
    while True:
        print("Minigames")
        print("Enter 1 for Pong \nEnter 2 for Hangman \nEnter 3 for Platform Game \nEnter 'Quit' to exit minigames")
        choice = input("Choose here: ")

        if choice == "1":
            game = Game()
            print("\n")
            game.run()
            main_menu()
        elif choice == "2":
            hangman()
            main_menu()
        elif choice == "3":
            game = Platform()
            print("\n")
            game.run()
            main_menu()
        elif choice.upper() != "QUIT":
            print("Invalid input, please type a valid input for one of the minigames or type 'quit' if you want to exit")
            main_menu()
        elif choice == "QUIT":
            choice=choice.upper()
            print("Thanks for playing the minigames!")
            break
        break





if __name__ == "__main__":
    main_menu()
