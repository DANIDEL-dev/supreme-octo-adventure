import time
import random
index = 0
template1 = ["In your hand is a rusty (but not very effective) AK47. \n\n",
             "In your hand is a rusty (but not very effective) Bazooka. \n\n",
             "In your hand is a rusty (but not very effective) Toygun. \n\n"]

template2 = ["You feel tensed for this battle,' with your rusty AK47 ' \n\n",
             "You feel tensed for this battle,' with your rusty Bzooka ' \n\n",
             "You feel tensed for this battle,' with your rusty Toygun ' \n\n"]
items = []


def print_pause(info):
    print(info)
    time.sleep(1)


def intro():
    print_pause("You find yourself in an open agbado-field,"
                " filled with thornes")
    print_pause("Rumor has it that a dragon called 'SAPA'"
                " is somewhere around here,\n"
                "and has been terrifying the nearby entire city.")
    print_pause("In front of you is a house ")
    print_pause("To your right is a dark, slippery and lonley cave ")
    print(random.choice(template1))


def decision_making():
    print_pause("Enter 1 to 'bang hard!!' on the door of the house.")
    print_pause("Enter 2 to peep into the cave ")
    print_pause("What would you like to do?")


def contact_before_cave1():
    print_pause("You approach the door of the house. ")
    print_pause("You are about to knock when the door,"
                " mysteriously disappears and out steps 'BIGFOOT!!! \n")
    print_pause("Ewehhh!!! This is Bigfoot's house!! \n")
    print_pause("Bigfoot attacks you! ")
    print(random.choice(template2))


def contact_before_cave2():
    print_pause("You do your best... ")
    print_pause("but your dagger is no match for Bigfoot. ")
    print_pause("You have been defeated! \n")


def cave_life1():
    print_pause("You peek  cautiously into the cave. ")
    print_pause("It turns out to be only a very small cave. ")
    print_pause("You notice a glint of  shiny metal behind a rock. ")
    print_pause("You have found the magical Grenade launcher"
                " of Anti-SAPA! called 'wazobia' ")
    print_pause("You discard your silly old weapon "
                "and take the Grenade Launcher with you. ")
    print_pause("You walk back out to the agbado-field. \n\n")
    items.append("wazobia")


def live_to_die_another_day():
    print_pause("You run back into the field. Luckily,"
                "you don't seem to have been followed. ")


def counter_attack():
    print_pause("As Bigfoot attacks, you aim your new wazobia.")
    print_pause("The magical Grenade launcher of Anti-SAPA!"
                "shines brightly as you brace for the attack.")
    print_pause("But Bigfoot takes one look"
                " at your shiny new toy and runs away!")
    print_pause("You have rid the city of BIGFOOT!."
                " You are victorious!")


def powerless_entry():
    contact_before_cave2()
    choice3 = input("Would you like to play again?"
                    " (y / n) \n").lower()
    if choice3 == "n":
        print_pause("Thanks for playing!"
                    " See you next time.")
    elif choice3 == "y":
        print_pause("Excellent! Restarting the game ... \n")
        adventure_game()


def poweful_entry():
    counter_attack()
    choice3 = input("Would you like to play again? (y / n)").lower()
    if choice3 == "n":
        print_pause("Thanks for playing! See you next time.")
    elif choice3 == "y":
        print_pause("Excellent! Restarting the game ...")
        adventure_game()


def cave_re_entry():
    print_pause("Nothing new here")
    print_pause("you walk back outside")
    cave_choice = input("I think we're done here..."
                        "press '1' to move on or '2' to "
                        "visit the  cave again. \n").lower()
    if cave_choice == "1":
        adventure_game_middle()
    elif cave_choice == "2":
        cave_re_entry()
    else:
        print_pause("Please try again ")
        choice1_2 = input("Invalid input detected."
                          "Kindly enter either '1' or '2' ")
        if cave_choice == "1":
            adventure_game_middle()
        elif cave_choice == "2":
            cave_re_entry()
        else:
            cave_wrong_input()


def try_again1():
    print_pause("Please try again ")
    choice1_2 = input("Invalid input detected."
                      "Kindly enter either '1' or '2' ")
    if choice1_2 == "1":
        powerless_entry()
    elif choice1_2 == "2":
        live_to_die_another_day()
        adventure_game_middle()


def try_again2():
    choice3 = input("Would you like to play again? (y / n)")
    if choice3 == "n":
        print_pause("Thanks for playing! See you next time.")
    elif choice3 == "y":
        print_pause("Excellent! Restarting the game ...")
        adventure_game()


def try_again3():
    print_pause("Please try again")
    print_pause("You don't seem focused..."
                "let's start from the begining again...")
    adventure_game()


def cave_wrong_input():
    print_pause("Please try again ")
    choice1_2 = input("Invalid input detected."
                      "Kindly enter either '1' or '2' ")
    if choice1_2 == "1":
        adventure_game_middle()
    elif choice1_2 == "2":
        cave_re_entry()
    else:
        cave_wrong_input()


def bad_option():
    contact_before_cave1()
    choice2 = input("Would you like to (1) fight"
                    " or (2) run away? \n")
    if choice2 == "1":
        powerless_entry()
    elif choice2 == "2":
        live_to_die_another_day()
        adventure_game_middle()
    else:
        print_pause("Please try again ")
        choice1_2 = input("Invalid input detected.\n"
                          "Kindly enter either '1' or '2' \n")
        if choice1_2 == "1":
            powerless_entry()
        elif choice1_2 == "2":
            live_to_die_another_day()
            adventure_game_middle()
        else:
            try_again1()


def good_option():
    cave_life1()
    choice1 = input("What would you like to do?\n"
                    "Please enter either 1 to approach the door \n"
                    "or\n" "2 to peep into the cave again \n").lower()
    if choice1 == "1":
        contact_before_cave1()
        choice2 = input("Would you like to (1)"
                        " fight or (2) run away? \n")
        if choice2 == "1":
            counter_attack()
            choice3 = input("Would you like to play again? (y / n) \n").lower()
            if choice3 == "n":
                print_pause("Thanks for playing! See you next time.")
            elif choice3 == "y":
                print_pause("Excellent! Restarting the game ...")
                adventure_game()
            else:
                print_pause("Please try again")
                choice2_2 = input("Invalid input detected.\n"
                                  "Kindly enter either 'y' or 'n' \n").lower()
                if choice2_2 == "n":
                    print_pause("Thanks for playing! See you next time.")
                elif choice2_2 == "y":
                    print_pause("Excellent! Restarting the game ...")
                    adventure_game()
                else:
                    try_again2()
    elif choice1 == "2":
        cave_re_entry()


def initial_option():
    print_pause("Please try again")
    choice3_1 = input("Invalid input detected.\n"
                      "Kindly enter either 'y' or 'n' \n").lower()
    if choice3_1 == "1":
        bad_option()
    elif choice3_1 == "2":
        good_option()
    else:
        initial_option()


def adventure_game():
    intro()
    decision_making()
    choice1 = input("Please enter either 1 or 2 \n").lower()
    if choice1 == "1":
        bad_option()
    elif choice1 == "2":
        good_option()
    else:
        initial_option()


def adventure_game_middle():
    decision_making()
    choice1 = input("Please enter either 1 or 2 \n").lower()
    if choice1 == "1":
        bad_option()
    elif choice1 == "2":
        good_option()
    else:
        initial_option()


adventure_game()
