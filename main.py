lost_light_house = "The Lost Lighthouse"
print(lost_light_house)

intro = """ this is a game where player wake up on a mystery island
after a deadly storm and there is light house that is dark and the bridge is also locked,
A rescue boat will arrive only if the player restores the lighthouse beacon. 
this game is for a player that explore locations, collects objects, solves simple
puzzles and either escapes or runs out of energy."""
print(intro)

player = input("What is your name: ")
print(f"{player}, you are welcome {lost_light_house}!")

starting_energy = 5
print(starting_energy)

current_energy = starting_energy
print(current_energy)

current_energy = current_energy - 1
print(current_energy)
print(starting_energy)

if current_energy > 0:
    print("Continue exploring")
else:
    print("Game over!")    