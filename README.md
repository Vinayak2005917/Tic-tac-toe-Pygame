# Pygame Tic Tac Toe

A classic Tic Tac Toe game built with Python and Pygame, featuring a graphical interface with custom assets and automatic game reset functionality.

## Features

- **Graphical Interface**: Clean visual design with custom board and player symbols
- **Two-Player Gameplay**: Alternating turns between Cross (Player 1) and Circle (Player 2)
- **Win Detection**: Automatically detects winning combinations (rows, columns, diagonals)
- **Draw Detection**: Recognizes when the board is full with no winner
- **Auto Reset**: Game automatically resets after 5 seconds when a game ends
- **Executable Build**: Includes PyInstaller configuration for creating standalone executables

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Dependencies
- pygame-ce==2.5.5
- pyinstaller==6.14.1 (for building executables)
- Additional packaging dependencies (see requirements.txt)

## Project Structure

```
tick-tac-toe-game/
├── main.py              # Main game logic
├── status_check.py      # Win/draw condition checking
├── requirements.txt     # Python dependencies
├── main.spec           # PyInstaller build configuration
├── assets/             # Game assets
│   ├── main_board.png  # Game board image
│   ├── Cross.jpg       # Cross player symbol
│   └── Circle.jpg      # Circle player symbol
└── Executable/         # Built executable files
```

## How to Play

1. **Run the game**: Execute `python main.py`
2. **Make moves**: Click on any empty cell to place your symbol
3. **Players alternate**: Cross goes first, then Circle
4. **Win conditions**: Get three symbols in a row (horizontal, vertical, or diagonal)
5. **Auto reset**: Game resets automatically after displaying results

## Game Controls

- **Mouse Click**: Place your symbol on the board
- **Close Window**: Exit the game

## Building an Executable

To create a standalone executable:

```bash
pyinstaller main.spec
```

The executable will be created in the `dist/` folder with all assets bundled.

## Code Structure

### Main Components

- **main.py**: Contains the main game loop, rendering, and input handling
- **status_check.py**: Implements [`win_check`](status_check.py) and [`draw_check`](status_check.py) functions
- **Asset Management**: Uses [`resource_path`](main.py) function for proper asset loading in both development and executable modes

### Key Functions

- **Game Logic**: Player turn management and move validation
- **Rendering**: Board state visualization and UI updates  
- **Win Detection**: Checks all possible winning combinations
- **Reset System**: Automatic game state reset after completion

## Technical Details

- **Display Size**: 480x560 pixels
- **Board Grid**: 3x3 grid with precise click detection
- **Asset Scaling**: Images are automatically scaled to fit board positions
- **Frame Rate**: Uses pygame's display update for smooth rendering

## Development

The game uses a simple state machine with the following states:
- Active gameplay (accepting moves)
- Game over (displaying results)
- Reset countdown (preparing for new game)

Board positions are tracked in a linear array (`board_state`) with indices 0-8 representing the 3x3 grid.
