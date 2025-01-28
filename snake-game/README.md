# Snake Game

Welcome to the Snake Game! This project is a fun and interactive game built using Python and the Turtle library. The goal of the game is to navigate the snake, eat food, and achieve the highest score possible without colliding with the walls or the snake's own body.

## Features

- **Dynamic Gameplay**: The snake grows longer with each piece of food it eats.
- **Colorful Food**: The food changes to a random color every time it spawns.
- **Score Tracking**: Keep track of your score as you play, with a game-over message displayed when the game ends.

## Prerequisites

To run this game, you'll need:

- Python 3.x installed on your system.
- The Turtle graphics library (pre-installed with Python).

## How to Play

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/HimkarSingh/snake-game.git
   cd snake-game
   ```
2. Run the game by executing the `main.py` file:
   ```bash
   python main.py
   ```
3. Use the arrow keys to control the snake:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right

4. Try to eat the food to grow your snake and increase your score. Avoid running into the walls or your own body.

## File Structure

- **main.py**: The main script that initializes the game and manages gameplay.
- **snake.py**: Contains the `Snake` class, which defines the behavior of the snake.
- **food.py**: Contains the `Food` class, responsible for spawning and refreshing the food.
- **scoreboard.py**: Contains the `Scoreboard` class, which displays and updates the score.

## Code Overview

### main.py
This file sets up the game window and handles game logic such as:
- Creating and controlling the snake.
- Detecting collisions with food and walls.
- Updating the score.

### snake.py
Defines the `Snake` class, including methods for:
- Moving the snake.
- Changing direction.
- Growing longer after eating food.

### food.py
Defines the `Food` class, responsible for:
- Spawning food at random locations.
- Assigning random colors to the food.

### scoreboard.py
Defines the `Scoreboard` class, which:
- Displays the current score on the screen.
- Shows a game-over message when the game ends.

## Demo
![Snake Game Demo](https://github.com/HimkarSingh/snake-game/blob/main/game_start.PNG)
### Game Over
![Game Over](https://github.com/HimkarSingh/snake-game/blob/main/game_over.PNG)

## Future Enhancements

- Add levels with increasing difficulty.
- Include sound effects.
- Implement a high-score leaderboard.

## Contributing

Contributions are welcome! If you have any ideas or suggestions, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy playing the Snake Game! 🐍

