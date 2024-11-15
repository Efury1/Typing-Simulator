import time
import sys
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
    print() # Add an extra blanl line after all lines are printing

def gather_user_input():
    print("Enter the script you want to simulate(type 'END' on a new line to finish):")
    user_input = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        user_input.append(line)
        
        if not user_input:            
            user_input = [
                "No Script Provided",
            ]
        return user_input
    
def main():
    user_input = gather_user_input()
    simulate_typing(user_input)

if __name__ == "__main__":
    main()