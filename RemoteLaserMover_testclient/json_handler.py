import json

# Initialize data structure
motor_values = [0, 0]

# Set motor value at motor index
def set_motor(device_index: int, value: int):
    motor_values[device_index] = value


# Get motor value from motor index
def get_motor(device_index: int):
    return motor_values[device_index]


# Return string form of data
def __str__():
    # Convert motor_values to JSON
    try:
        json_data = json.JSONEncoder.encode({"motor_values": motor_values})
    
    except json.JSONDecodeError:
        print("Error: Could not encode data.")
    
    # Serialize data
    string_data = json.dumps(json_data)
    
    return string_data