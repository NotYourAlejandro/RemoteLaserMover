import serial
import sys

program_file_name = sys.argv[0]

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
    
    # Extract the data from args
    port = parse_args_port()
    
    # Enter into shell
    serial_shell()
    
    # Goodbye message
    print("Goodbye!")
    

def serial_shell():
    loop_continue = True
    motor_low_range = 0
    motor_high_range = 181
    motor_range = range(motor_low_range, motor_high_range)
    
    while loop_continue:
        # Get the input
        print("Enter a value to set the motor to. -1 to stop.\n> ", end="")
        user_input = input()
        
        # Convert the string into an int
        try:
            user_value = int(user_input)
        
        except ValueError:
            eprint("Error: Value is not an integer.\n")
            continue
        
        # Escape case
        if user_value == -1:
            loop_continue = False
            continue
        
        # Determine if number is in range
        if user_value not in motor_range:
            eprint(f"Error: Value is not in range. Range: {motor_low_range} to {motor_high_range - 1}.\n")
            continue
        
        # Convert entry to JSON
        
        
        # Send data over serial
        
        
        
        
def parse_args_port() -> str:
    """Parses the program arguments for the port.

    Returns:
        str: Path of port
    """
    
    # get the argument contents
    port_argument = ""
    
    for i, arg in enumerate(sys.argv):
        if "--port=" in arg:
            port_argument = arg
    
    # Remove the "--port="
    if '"' in port_argument:
        port = port_argument[8:-1]
    else:
        port = port_argument[7:]
    
    return port


def eprint(*args, **kwargs):
    """This function is an abstraction to print to stderr easily.
    """
    print(*args, file=sys.stderr, **kwargs)


main()