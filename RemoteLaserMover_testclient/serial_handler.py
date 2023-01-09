"""This module is created to remove the need to handle the serial object from
   other modules.
"""

import serial

connection: serial.Serial = None

def set_device(device_path: serial.Serial):
    """Sets the device to connect to.

    Args:
        device_path (str): Path of device to connect to
    """
    
    connection = device_path
    

def send_string_over_serial(data: str):
    """Send a string over serial.

    Args:
        data (str): Data to send over serial.
    """
    
    if connection == None:
        print("Error: No connection established.")
        return
    
    connection.write(data)