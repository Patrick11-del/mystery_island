lost_light_house = "The Lost Lighthouse"
print(lost_light_house)

intro = """ this is a game where player wake up on a mystery island
after a deadly storm and there is light house that is dark and the bridge is also locked,
A rescue boat will arrive only if the player restores the lighthouse beacon. 
this game is for a player that explore locations, collects objects, solves simple
puzzles and either escapes or runs out of energy."""
print(intro)

player_name = input("What is your name: ")
print(f"{player_name}, you are welcome {lost_light_house}!")

player_state = {
    "name": player_name,
    "location": "Beach",
    "energy": 5,
    "inventory": [],
    "game_over": False,
    "won": False

}
# current_energy = current_energy - 1
# print(current_energy)
# print(starting_energy)

# if current_energy > 0:
#     print("Continue exploring")
# else:
#     print("Game over!")   

# has_rope = True
# if has_rope and current_energy > 0:
#     print("Crossing is allowed") 
# else:
#     print("Crossing not allowed") 

next_location = {
    "Beach": "Jungle",
    "Jungle": "Cave",
    "Cave": "Old_bridge",
    "Old_bridge": "Lighthouse"
}


game_running = True
while game_running:
    
    print("1. Explore")
    print("2. Check energy")
    print("3. Check inventory")
    print("4. Collect rope")
    print("5. Quit")

    player_choice = input("Enter choice :")

    if player_choice == "1":
        if player_state["energy"] > 0:
            current_location = player_state["location"]

            if current_location in next_location["location"]:
                destination = next_location[current_location]

                player_state["location"] = destination

                player_state["energy"] -= 1
                print(f"You are now at {destination}") 
                print(f"remaining energy: {player_state['energy']}")
            else:
                print("There is no location to explore")
        else:
            print("you have run out of energy!")             

    elif player_choice == "2":
        print(f"You have {player_state['energy']} remaining!") 

    elif player_choice == "3":
        print(f"Your inventory list: {player_state['inventory']}") 

    elif player_choice == "4":
        if "rope" not in player_state["inventory"]:
            player_state["inventory"].append("rope")
            print("You collected a rope!")
        else:
            print("You already has a rope!")    

    elif player_choice == "5":
        game_running = False       
    else:
        print("Your choice is invalid!") 
print("Thank you for playing, Goodbye!")

