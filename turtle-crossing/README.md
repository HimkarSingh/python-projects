# Turtle Crossing Game

Welcome to the Turtle Crossing Game! This is a fun and engaging Python project that challenges the player to guide a turtle across a busy road without getting hit by cars. Each successful crossing advances the player to the next level, increasing the game's difficulty.

---

## Features

- **Player Movement**: Use the up arrow key to move the turtle forward.
- **Randomly Generated Cars**: Cars of varying colors appear randomly and move across the screen.
- **Increasing Difficulty**: With each successful crossing, the cars move faster, making the game more challenging.
- **Score Tracking**: The current level is displayed on the screen, and a "Game Over" message appears if the turtle collides with a car.

---

## Prerequisites

To play this game, you'll need:

- Python 3.x installed on your system.
- The Turtle graphics library (pre-installed with Python).

---

## How to Play

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/HimkarSingh/turtle-crossing-game.git
   cd turtle-crossing-game
   ```

2. Run the game by executing the `main.py` file:

   ```bash
   python main.py
   ```

3. Controls:

   - Press the **Up Arrow** key to move the turtle forward.

4. Avoid the cars and guide the turtle to the top of the screen to level up.

5. If the turtle collides with a car, the game ends.

---

## File Structure

- **main.py**: Initializes the game window and manages the main game loop.
- **player.py**: Contains the `Player` class, which handles the turtle's movement and position.
- **car\_manager.py**: Manages the cars, including creation, movement, and speed adjustments.
- **scoreboard.py**: Tracks and displays the player's current level and displays the "Game Over" message.

---

## Code Overview

### main.py

This is the main file that:

- Sets up the game screen and initializes game components.
- Listens for player input to move the turtle.
- Manages the main game loop, including car movement, collision detection, and level progression.

### player.py

Defines the `Player` class, which:

- Handles the turtle's movement.
- Resets the turtle's position upon successful crossing.
- Checks if the turtle has reached the finish line.

### car\_manager.py

Defines the `CarManager` class, which:

- Creates and manages cars with random colors and positions.
- Moves cars across the screen and increases their speed with each level.
- Includes functionality to adjust car generation for higher difficulty.

### scoreboard.py

Defines the `Scoreboard` class, which:

- Displays the current level on the screen.
- Updates the level dynamically as the player progresses.
- Displays a "Game Over" message if the turtle collides with a car.

---

## Screenshots

### Start of the Game
![Start Game](https://github.com/HimkarSingh/turtle-crossing/blob/main/start_game.PNG)

### Game Over Screen
![Game Over](https://github.com/HimkarSingh/turtle-crossing/blob/main/game_over.PNG)

---

## Future Enhancements

- Add sound effects for car collisions and successful crossings.
- Implement additional difficulty settings or levels.
- Introduce power-ups or bonuses for the player.
- Create a high-score tracker.

---

## Contributing

Contributions are welcome! If you have ideas for improvement or new features, feel free to fork this repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy the game and see how many levels you can complete! 😎🌊

