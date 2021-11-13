import random
import time

print("\nWelcome to Hangman :) \n")
name = input("Enter your name: ")
print("Hello " + name + " ALL THE BEST")
time.sleep(2)
print("The game will start soon be readyyyy :V !\nLet's play Hangman!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global key
    global already_guessed
    global length
    global play_game
  

    words = {'Flowers' : ["lotus","lily","rose","orchid","sunflower","tulip","daisy","jasmine","hibiscus","champa","creeper","merrygold","rajnigandha"],
             'Animals' : ["tiger","lion","cow","bufflow","goat","pig"],
             'Months'  : ["january","february","march","april","may","june","july","august","september","october","november","december"]
            }
    key=random.choice(list(words))
    print(key)
    word = random.choice(words[key])
    print(word)
    # word=random.choice(list(words))
    # word = random.choice(words)
    length = len(word)
    count = 0
    display = '_' * length
    display2 = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n"+"Hint:"+"The word is a name of "+ key +"\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   ___ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   ___ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "_|_\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "_|_\n")
            print("Sorry Wrong answer :(. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("WOWWW You DID IT! :D")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()