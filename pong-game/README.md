# Ping Pong Game 🎮

Welcome to the Ping Pong Game! 🏓 This is a classic two-player game implemented in Python using the Turtle graphics library. The objective is to score points by making your opponent miss the ball. 🎯

## Features

- **Two-Player Gameplay**: Control paddles on either side of the screen to hit the ball. ✨
- **Dynamic Ball Movement**: The ball increases speed after each paddle hit. 🚀
- **Score Tracking**: Keep track of points for both players, with scores displayed on the screen. 📊
- **Middle Dash Line**: A visual dashed line divides the playing field for better orientation. ⚡

## Prerequisites

To run this game, you'll need: 🛠️

- Python 3.x installed on your system.
- The Turtle graphics library (pre-installed with Python).

## How to Play

1. Clone this repository to your local machine. 🖥️
   ```bash
   git clone https://github.com/HimkarSingh/ping-pong-game.git
   cd ping-pong-game
   ```
2. Run the game by executing the `main.py` file:
   ```bash
   python main.py
   ```
3. Player controls:
   - **Right Paddle**:
     - Move Up: Arrow key "Up"
     - Move Down: Arrow key "Down"
   - **Left Paddle**:
     - Move Up: Key "W"
     - Move Down: Key "S"

4. Try to hit the ball with your paddle to prevent your opponent from scoring. 🎮 The game ends when a player decides to stop.

## File Structure

- **main.py**: Initializes the game window and handles overall game logic. 📂
- **paddle.py**: Contains the `Paddle` class and the `dash_line` function for creating paddles and the center line. 🏓
- **ball.py**: Defines the `Ball` class, which manages ball movement and collision detection. ⚙️
- **scoreboard.py**: Contains the `Scoreboard` class for updating and displaying the score. 📈

## Code Overview

### main.py
Sets up the game window, initializes paddles, the ball, and the scoreboard, and handles the main game loop. 🔄

- Detects collisions with walls and paddles.
- Resets the ball's position and updates the score when a player misses the ball.

### paddle.py
Defines the `Paddle` class and the `dash_line` function: 🛠️

- **Paddle Class**:
  - Controls paddle movement.
  - Supports positioning paddles on either side of the screen.
- **dash_line Function**:
  - Draws a dashed line in the middle of the screen.

### ball.py
Defines the `Ball` class: ⚙️

- Handles ball movement and bouncing mechanics.
- Resets the ball to the center when a player misses.

### scoreboard.py
Defines the `Scoreboard` class: 🏆

- Tracks and displays scores for both players.
- Updates the score dynamically during gameplay.

## Demo
![Ping Pong Game Demo](https://your-image-link-here) 🌟

## Future Enhancements

- Add sound effects for ball collisions and scoring. 🔊
- Introduce levels or difficulty settings. 📈
- Implement single-player mode with AI-controlled paddle. 🤖

## Contributing

Contributions are welcome! 🌟 If you have ideas or suggestions, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details. 📝

---

Enjoy the game and challenge your friends to a match of Ping Pong! 🏓😊

