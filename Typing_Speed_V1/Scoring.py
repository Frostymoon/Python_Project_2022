import Screen
# fixme code runs twice and i have no idea how / why
def difficulty_check():
    difficulty = "input('How good are you?\n')"
    match difficulty:
        case "1":
            print("Well at least you're aware of your skills. Here we go!")
        case "2":
            print("Most people lie int this bracket and you're no different. Not standing out at all...")
        case "3":
            print("Well look who's confident in themselves! Ok, hotshot. Let's see what you've got.")
        case "4":
            print("Quidquid Latine dictum sit, altum videtur\nAMEN")
        case _ :
            print("Started strong right out the gates, huh... How 'bout you givbe it another go.")
            # difficulty_check()
            
difficulty_check()