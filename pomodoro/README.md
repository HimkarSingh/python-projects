# Pomodoro Timer

The **Pomodoro Timer** is a simple and effective productivity tool built using Python and Tkinter. It helps users manage their time efficiently by breaking work into focused intervals (Pomodoros) separated by short and long breaks.

---

## Features

- **Work Intervals**: Focused 25-minute work sessions.
- **Breaks**: Short 5-minute breaks and a long 20-minute break after every 4 work intervals.
- **Visual Countdown**: A dynamic timer displayed with a tomato icon.
- **Session Tracker**: Tracks completed work sessions using checkmarks.
- **Reset Functionality**: Allows users to reset the timer at any point.

---

## Prerequisites

To use the Pomodoro Timer, ensure you have:

- **Python 3.x** installed on your system.
- The `Tkinter` library (pre-installed with Python).

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/HimkarSingh/pomodoro.git
   cd pomodoro
   ```

2. Place the `tomato.png` image file in the project directory.

3. Run the application:

   ```bash
   python main.py
   ```

---

## How It Works

1. **Start the Timer**: Click the **Start** button to initiate the timer.
2. **Work and Break Intervals**: The timer will automatically switch between work intervals (25 minutes) and breaks (5 or 20 minutes).
3. **Track Progress**: Checkmarks appear below the timer to indicate completed work sessions.
4. **Reset**: Use the **Reset** button to stop the timer and clear progress.

---

## Code Overview

### Constants
- Defined colors, font styles, and time durations for work and break intervals.

### Functions
1. **reset_timer()**: Resets the timer, progress, and UI labels.
2. **start_timer()**: Determines whether it’s a work or break interval and initiates the countdown.
3. **count_down()**: Handles the countdown mechanism and updates the UI dynamically.

### UI Setup
- Created using Tkinter with a tomato image for visual appeal.
- Buttons and labels are arranged to ensure an intuitive user experience.

---

## Future Enhancements

- Add sound notifications for session transitions.
- Implement a feature to customize work and break durations.
- Save session data to track long-term productivity.

---

## Screenshots

### Timer at Start
![Start Timer](https://github.com/HimkarSingh/pomodoro/blob/main/start_timer.PNG)

### Timer During Work Interval
![Work Timer](https://github.com/HimkarSingh/pomodoro/blob/main/work_timer.png)

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

**Stay focused and productive with the Pomodoro Timer!**

