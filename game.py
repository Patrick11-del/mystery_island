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

    return "Invalid action."