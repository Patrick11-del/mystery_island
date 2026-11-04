
from game import new_game
from game import new_game, apply_action


lost_light_house = "The Lost Lighthouse"
print(lost_light_house)

intro = """This is a game where a player wakes up on a mystery island
after a deadly storm. The lighthouse is dark and the bridge is locked.
A rescue boat will arrive only if the player restores the lighthouse beacon.
The player explores locations, collects objects, solves simple
puzzles and either escapes or runs out of energy."""
print(intro)

player_name = input("What is your name: ")
print(f"{player_name}, you are welcome to {lost_light_house}!")

player_state = new_game(player_name)

next_location = {
    "Beach": "Jungle",
    "Jungle": "Cave",
    "Cave": "Old bridge",
    "Old bridge": "Lighthouse"
}

game_running = True

while game_running:

    print("\n1. Explore")
    print("2. Check energy")
    print("3. Check inventory")
    print("4. Collect rope")
    print("5. Collect lantern")
    print("6. Quit")
    print("7. Search the Jungle for clues")
    print("8. Restore lighthouse beacon")

    player_choice = input("Enter choice: ")

    # OPTION 1: EXPLORE
    if player_choice == "1":

        if player_state["energy"] > 0:

            current_location = player_state["location"]

            if current_location in next_location:

                destination = next_location[current_location]
                if destination == "Old bridge" and "lantern" not in player_state["inventory"]:
                    print("You must collect the lantern in the Cave first!")
   

                elif destination == "Lighthouse" and "rope" not in player_state["inventory"]:
                    print("You cannot proceed without a rope!")

                else:
                    player_state["location"] = destination
                    player_state["energy"] -= 1

                    print(f"You are now at {destination}")
                    print(f"Remaining energy: {player_state['energy']}")

                    if player_state["energy"] == 0:
                        player_state["game_over"] = True
                        game_running = False
                        print("You have run out of energy. Game over!")

            else:
                print("There is no more location to explore.")

        else:
            player_state["game_over"] = True
            game_running = False
            print("You have run out of energy. Game over!")

    # OPTION 2: CHECK ENERGY
    elif player_choice == "2":
        print(f"You have {player_state['energy']} energy remaining!")

    # OPTION 3: CHECK INVENTORY
    elif player_choice == "3":
        print(f"Your inventory: {player_state['inventory']}")

    # OPTION 4: COLLECT ROPE
    elif player_choice == "4":

        if player_state["location"] != "Beach":
            print("Rope must be collected at the Beach.")

        elif "rope" not in player_state["inventory"]:
            player_state["inventory"].append("rope")
            print("You collected a rope!")

        else:
            print("You already have a rope!")

    # OPTION 5: COLLECT LANTERN
    elif player_choice == "5":

        if player_state["location"] != "Cave":
            print("The lantern can only be collected at the Cave.")

        elif "lantern" not in player_state["inventory"]:
            player_state["inventory"].append("lantern")
            print("You collected a lantern!")

        else:
            print("You already have a lantern!")

    # OPTION 6: QUIT
    elif player_choice == "6":
        game_running = False

    # OPTION 7: SEARCH THE JUNGLE
    elif player_choice == "7":

        if player_state["location"] != "Jungle":
            print("You are not in the Jungle.")

        elif player_state["searched_jungle"]:
            print("You have already searched the Jungle.")

        elif player_state["energy"] < 2:
            print("You do not have enough energy to search.")

        else:
            player_state["energy"] -= 2
            player_state["searched_jungle"] = True

            print("You found a clue!")
            print("The lantern is hidden in the Cave.")
            print("A rope is required to cross the Old Bridge.")

            if player_state["energy"] == 0:
                player_state["game_over"] = True
                game_running = False
                print("You have run out of energy. Game over!")

    # OPTION 8: RESTORE LIGHTHOUSE BEACON
    elif player_choice == "8":

        if player_state["location"] == "Lighthouse" and "lantern" in player_state["inventory"] and player_state["energy"] > 0:

            player_state["won"] = True
            player_state["game_over"] = True
            game_running = False

            print("Congratulations! You have successfully completed the game!")
            print("The lighthouse beacon is restored!")
            print("The rescue boat is coming!")

        else:
            print("You cannot restore the lighthouse beacon yet.")

            if player_state["location"] != "Lighthouse":
                print("You must reach the Lighthouse first.")

            elif "lantern" not in player_state["inventory"]:
                print("You need a lantern to restore the beacon.")

            elif player_state["energy"] <= 0:
                print("You have no energy remaining.")

    # INVALID MENU CHOICE
    else:
        print("Your choice is invalid!")

print("\nThank you for playing The Lost Lighthouse!")