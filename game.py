# GAME
import random

options = ("piedra", "papel", "tijera")
computer_wins = 0
user_wins = 0
rounds = 1


while True:
    print("*"*10)
    print("ROUND", rounds)
    print("*"*10)

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)

    user_option = input("piedra papel o tijera=> ")
    user_option = user_option.lower()

    if not user_option in options:
        print("esa opcion no es valida")
        continue

    pc_option = random.choice(options)

    # OPTIONS
    print("User option => ", user_option)
    print("Computer option =>", pc_option)

    # REGLAS
    if user_option == pc_option:
        print("Empate")

    elif user_option == "piedra":
        if pc_option == "tijera":
            print("piedra gana tijera, user gana")
            user_wins += 1
        else:
            print("papel gana piedra, gana pc")
            computer_wins += 1
    elif user_option == "papel":
        if pc_option == "piedra":
            print("user gana!")
            user_wins += 1
        else:
            print("computador gana")
            computer_wins += 1
    elif user_option == "tijera":
        if pc_option == "papel":
            print("gana user")
            user_wins += 1
        else:
            print("gana pc")
            computer_wins += 1

    if computer_wins == 2:
        print("ganador final es computadora")
        break
    if user_wins == 2:
        print("ganador final es usuario")
        break

    rounds += 1
