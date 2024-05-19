# Break Reminder Script

This Python script is designed to help users maintain healthy work habits by reminding them to take regular breaks while working on the computer. It prompts users to take short breaks after a certain duration of work, helping to reduce eye strain, fatigue, and improve productivity.

## Features

- **Interval Breaks:** After every two intervals of work (each interval configurable), the script prompts the user to take a short break.
- **Extended Break:** After a predefined number of interval breaks, the script suggests an extended break to allow for relaxation and rejuvenation.
- **Cross-Platform:** The script is compatible with both Windows and Unix-like systems, ensuring a consistent experience across different platforms.
- **Minimal User Interaction:** The script runs in the background, requiring minimal user interaction. Users can opt to extend breaks if needed or confirm their readiness to resume work.
- **Customizable Settings:** Users can easily customize the duration of work intervals, break durations, and other settings to suit their preferences.

## Installation

To use the script, follow these steps:

1. **Clone the Repository:**
   git clone https://github.com/on404/remainder.git 
2. **Navigate to the Directory:**
   cd remainder

3. **Run the Script:**
- For Windows:
  ```
  python reminder.py
  ```
- For Unix-like systems:
  ```
  python3 reminder.py
  ```

## Usage

1. **Start the Script:**
- Run the script either manually or configure it to run automatically on system startup (instructions provided in the script).

2. **Work Intervals:**
- The script measures work intervals (default: 3 seconds) and prompts the user to take a short break after every two intervals.

3. **Break Reminders:**
- When it's time for a break, a popup window appears with options to extend the break or confirm readiness to resume work.

4. **Extended Breaks:**
- After a predefined number of short breaks, the script suggests an extended break (default: 2 hours).

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to open an issue or submit a pull request. Your feedback and contributions help make this script more useful for everyone.

## License

This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code for both commercial and non-commercial purposes. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Special thanks to contributors and open-source libraries that made this project possible.

Happy coding and remember to take breaks!
 
