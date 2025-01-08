# Mini_Projects_using_Python
Mini Projects using Python

1. YEAR CALENDER GENERATOR.
2. STOP WATCH.

---------------------------------------------------------------------------------------------------------------------------------------------------------

# Python Time Applications

This repository contains two Python applications built using Tkinter: a Digital Calendar and a Digital Stopwatch. Both applications provide user-friendly graphical interfaces for time-related functionalities.

## Applications Overview

### 1. Digital Calendar (`calendar.py`)

A simple calendar application that allows users to view and save calendar layouts for specific months.

#### Features:
- View calendar for any specified year and month
- Save calendar layout to a text file
- Input validation for year and month entries
- Error handling for invalid inputs

#### How It Works:

The calendar application is structured around these main components:

1. **User Interface Components:**
   - Input fields for year and month
   - Display area for calendar
   - Buttons for showing and saving the calendar
   - Error message dialogs for invalid inputs

2. **Core Functions:**
   - `display_calendar(year, month)`: Generates and displays the calendar layout
   - `save_calendar()`: Exports the current calendar view to a text file
   - `show_calendar()`: Validates input and triggers calendar display

3. **Program Flow:**
   ```
   User Input → Input Validation → Calendar Generation → Display/Save
   ```

The application uses Python's built-in `calendar` module to generate the calendar layout and Tkinter's `filedialog` for file saving operations.

### 2. Digital Stopwatch (`current_time.py`)

A feature-rich stopwatch application with lap timing functionality.

#### Features:
- Start, pause, and reset functionality
- Lap time recording
- 24-hour format display
- List view for recorded lap times

#### How It Works:

The stopwatch is implemented as a class-based application with the following structure:

1. **Class Components:**
   - `Stopwatch` class managing the entire application
   - Time tracking variables (hours, minutes, seconds)
   - UI elements (labels, buttons, listbox)

2. **Core Methods:**
   - `update_clock()`: Updates the time display every second
   - `start()`: Begins time counting
   - `pause()`: Halts time counting
   - `reset()`: Resets all values to zero
   - `lap()`: Records current time as a lap

3. **Program Flow:**
   ```
   Initialize UI → Time Update Loop → User Interactions → Display Updates
   ```

The stopwatch uses Tkinter's `after` method to create a recurring update cycle every 1000ms (1 second).

## Technical Implementation Details

### Calendar Application
- Uses `calendar.TextCalendar()` for generating formatted month layouts
- Implements error handling for:
  - Non-numeric inputs
  - Invalid month values (outside 1-12 range)
- File operations use context managers (`with` statements) for safe file handling
- Modal dialogs for user feedback and error messages

### Stopwatch Application
- Object-oriented design with a single `Stopwatch` class
- Time tracking using internal counters rather than system time
- Automatic rollover handling (seconds → minutes → hours)
- Thread-safe implementation for UI updates
- Persistent display updates using `root.after()`

## Dependencies
- Python 3.x
- Tkinter (usually comes with Python installation)
- Standard library modules: `calendar`, `time`, `threading`

## Usage

### Calendar Application:
1. Run `python calendar.py`
2. Enter the desired year and month
3. Click "Show Calendar" to view
4. Optionally click "Save Calendar" to export

### Stopwatch Application:
1. Run `python current_time.py`
2. Use the buttons to:
   - Start: Begin time counting
   - Pause: Stop time counting
   - Reset: Clear all times
   - Lap: Record current time

## Note
Both applications are standalone and can run independently. They showcase different aspects of Python GUI programming using Tkinter and provide practical utilities for time-related tasks.
