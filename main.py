
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

game_running = True

while game_running and not player_state["game_over"]:

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
        message = apply_action(player_state, "explore")
        print(message)
        

    # OPTION 2: CHECK ENERGY
    elif player_choice == "2":
        print(f"You have {player_state['energy']} energy remaining!")

    # OPTION 3: CHECK INVENTORY
    elif player_choice == "3":
        print(f"Your inventory: {player_state['inventory']}")

    # OPTION 4: COLLECT ROPE
    elif player_choice == "4":
        message = apply_action(player_state, "collect_rope")
        print(message)

    # OPTION 5: COLLECT LANTERN
    elif player_choice == "5":
        message = apply_action(player_state, "collect_lantern")
        print(message)

    # OPTION 6: QUIT
    elif player_choice == "6":
        game_running = False

    # OPTION 7: SEARCH THE JUNGLE
    elif player_choice == "7":
        message = apply_action(player_state, "search_jungle")
        print(message)
    # OPTION 8: RESTORE LIGHTHOUSE BEACON
    elif player_choice == "8":
        message = apply_action(player_state, "restore_beacon")
        print(message)
    # INVALID MENU CHOICE
    else:
        print("Your choice is invalid!")

print("\nThank you for playing The Lost Lighthouse!")