import time
import sys
import os
from colorama import Fore, Style

def simulate_typing(code_lines, line_delay=0.5, char_delay=0.05):
    """
    Simulate typing out code line by line with delays!
    This has been developed for Youtube videos.

    :param code_lines: List of code lines to "type out"
    :param line_delay: Delay between lines (in seconds)
    :param char_delay: Delay between characters (in seconds)
    """
    for line in code_lines:
        for char in line:
            sys.stdout.write(Fore.GREEN + char + Style.RESET_ALL)  # Print character without a newline
            sys.stdout.flush()  # Ensure the character is displayed immediately
            time.sleep(char_delay)  # Delay for typing effect
        print()  # Move to the next line after finishing the current one
        time.sleep(line_delay)  # Delay between lines
    print()  # Add an extra blank line after all lines are printed

def gather_user_input_from_file(file_path):
    """
    Gather user input from a text file.

    :param file_path: Path to the text file containing the code
    :return: List of code lines
    """
    try:
        with open(file_path, 'r') as file:
            code_lines = file.readlines()
            return [line.rstrip('\n') for line in code_lines]  # Keep exact spacing, remove only trailing newlines
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return ["No Script Provided"]

def main():
    # Set the path to your Notepad text file in the same directory as this script
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
    file_path = os.path.join(script_directory, "example.txt")  # Path to 'script.txt' in the same directory

    # Get user input from the specified file
    user_input = gather_user_input_from_file(file_path)

    # Simulate typing
    simulate_typing(user_input)

if __name__ == "__main__":
    main()
