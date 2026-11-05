# The Lost Lighthouse

## 1. Project Description

The Lost Lighthouse is a beginner-friendly, text-based Python adventure game.

The player wakes up on a mysterious island after a storm. The Lighthouse beacon has stopped working, and the player must complete a mission to restore it so that a rescue boat can find the island.

To complete the mission, the player explores different locations, collects useful objects, discovers clues, and manages their energy. The player wins by restoring the Lighthouse beacon or loses when their energy runs out.

## 2. Requirements

  Python 3

## 3. How to Run

Open your terminal in the project folder and run:

   bash
python3 main.py
```

## 4. Game Rules

- **Energy:** The player's limited resource. The player starts with 5 energy. Exploring costs 1 energy, while searching the Jungle costs 2 energy.
- **Locations:** The five places the player can explore: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- **Rope:** An object collected at the Beach. It is required to cross from the Old Bridge to the Lighthouse.
- **Lantern:** An object collected in the Cave. It is required to leave the Cave and continue towards the Old Bridge.
- **Winning:** The player wins by reaching the Lighthouse and restoring the beacon with a lantern while still having energy.
- **Losing:** The player loses when their energy reaches zero before restoring the beacon.

## 5. How to Run Tests

From the project folder, run:

```bash
python3 -m unittest discover -s tests -v
```

This command runs the automated tests for the game.

## 6. Known Limitations

- The game runs in the terminal and does not have a graphical interface.
- Game progress is not saved after the player exits.
- The player follows a predefined route rather than exploring an open-world map.

## 7. Project Structure

```text
mystery_island/
├── main.py
├── game.py
├── README.md
└── tests/
    └── test_game.py
```