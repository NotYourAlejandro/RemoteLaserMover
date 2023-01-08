import serial
import sys

program_file_name = "main.py"

def main():
    # Check for necessary commandline arguments
    args_contain_port = False
    
    for arg in sys.argv:
        if "--port=" in arg:
            args_contain_port = True
    
    # Display error if incorrect arguments supplied
    if not args_contain_port:
        print(f"Usage: {program_file_name} --port=[port here]")
        print(f"Example: {program_file_name} --port=/dev/ttyACM0")

def eprint(*args, **kwargs):
    """This function is an abstraction to print to stderr easily.
    """
    print(*args, file=sys.stderr, **kwargs)

main()