next_location = {
    "Beach": "Jungle",
    "Jungle": "Cave",
    "Cave": "Old bridge",
    "Old bridge": "Lighthouse"
}

def new_game(player_name):

    player_state = {
        "name": player_name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
        "searched_jungle": False
    }
    return player_state

def apply_action(player_state, action):

    if player_state["game_over"]:
        return "The game has already ended." 

    if action == "explore":

        if player_state["energy"] <= 0:
            player_state["game_over"] = True
            return "You have run out of energy. Game over!"

        current_location = player_state["location"]

        if current_location not in next_location:
            return "There is no more location to explore."

        destination = next_location[current_location]

        if destination == "Old bridge" and "lantern" not in player_state["inventory"]:
            return "You must collect the lantern in the Cave first!"

        elif destination == "Lighthouse" and "rope" not in player_state["inventory"]:
            return "You cannot proceed without a rope!"

        player_state["location"] = destination
        player_state["energy"] -= 1

        if player_state["energy"] == 0:
            player_state["game_over"] = True
            return (
                f"You are now at {destination}. "
                "You have run out of energy. Game over!"
            )

        return (
            f"You are now at {destination}. "
            f"Remaining energy: {player_state['energy']}"
        )

    elif action == "collect_rope":

        if player_state["location"] != "Beach":
            return "Rope must be collected at the Beach."

        elif "rope" in player_state["inventory"]:
            return "You already have a rope!"

        else:
            player_state["inventory"].append("rope")
            return "You collected a rope!"    

    elif action == "collect_lantern":
        if player_state["location"] != "Cave":
            return "The lantern can only be collected at the Cave."

        elif "lantern" in player_state["inventory"]:
            return "You already have a lantern!"

        else:
            player_state["inventory"].append("lantern")
            return "You collected a lantern!"
    
    elif action == "search_jungle":

        if player_state["location"] != "Jungle":
            return "You are not in the Jungle."

        elif player_state["searched_jungle"]:
            return "You have already searched the Jungle."

        elif player_state["energy"] < 2:
            return "You do not have enough energy to search."

        else:
            player_state["energy"] -= 2
            player_state["searched_jungle"] = True

            if player_state["energy"] == 0:
                player_state["game_over"] = True

                return (
                    "You found a clue!\n"
                    "The lantern is hidden in the Cave.\n"
                    "A rope is required to cross the Old Bridge.\n"
                    "You have run out of energy. Game over!"
                )

            return (
                "You found a clue!\n"
                "The lantern is hidden in the Cave.\n"
                "A rope is required to cross the Old Bridge."
            )

    elif action == "restore_beacon":

        if player_state["location"] != "Lighthouse":
            return "You must reach the Lighthouse first."

        elif "lantern" not in player_state["inventory"]:
            return "You need a lantern to restore the beacon."

        elif player_state["energy"] <= 0:
            return "You have no energy remaining."

        else:
            player_state["won"] = True
            player_state["game_over"] = True

            return (
                "Congratulations! You have successfully completed the game!\n"
                "The lighthouse beacon is restored!\n"
                "The rescue boat is coming!"
            )              


    return "Invalid action."

def is_win(player_state):
    return player_state["won"]   

def available_actions(player_state):

    if player_state["game_over"] or player_state["energy"] <= 0:
        return []

    actions = []
    location = player_state["location"]
    inventory = player_state["inventory"]

    if location in next_location:
        destination = next_location[location]

        if destination == "Old bridge" and "lantern" not in inventory:
            pass

        elif destination == "Lighthouse" and "rope" not in inventory:
            pass

        else:
            actions.append("explore")

    if location == "Beach" and "rope" not in inventory:
        actions.append("collect_rope")

    if location == "Cave" and "lantern" not in inventory:
        actions.append("collect_lantern")

    if location == "Jungle" and not player_state["searched_jungle"] and player_state["energy"] >= 2:
        actions.append("search_jungle")

    if location == "Lighthouse" and "lantern" in inventory:
        actions.append("restore_beacon")

    return actions    
