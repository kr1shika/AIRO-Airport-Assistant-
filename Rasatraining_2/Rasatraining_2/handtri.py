import serial
import time
ser = serial.Serial('COM7', 115200)  # Replace 'COM3' with the correct port for your setup
time.sleep(2)  # Wait for the connection to initialize

# Function to send the handwave command
def send_handwave_command():
    ser.write(b'now_wave')  # Send the character 'h' to the Arduino
    print("Handwave command sent.")


# Send the handwave command
send_handwave_command()

# Close the serial connection
ser.close()
