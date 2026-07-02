import serial
import time
import subprocess
import sys

# Replace 'COM15' with your actual port (e.g., '/dev/ttyUSB0' on Linux/Mac)
comport = "COM15"

# Check if an argument was passed
if len(sys.argv) > 1:
    print(f"Script name: {sys.argv[0]}")
    print(f"COM port: {sys.argv[1]}")
    comport = sys.argv[1]
else:
    print("Using the default: ",comport)

def get_REPL():
        ser.write(b'\x03')  # Ctrl+C
        time.sleep(0.1)
        ser.write(b'\x03')  # Ctrl+C safely twice
        time.sleep(0.1)
        ser.write(b'\x01')  # Ctrl+A forces Raw REPL mode
        time.sleep(0.1)
        ser.read_all()      # Clear the acknowledgment bytes from the buffer
try:
    now = time.localtime()
    time_string = f"TIME {now.tm_year},{now.tm_mon},{now.tm_mday},{now.tm_hour},{now.tm_min},{now.tm_sec},0,{now.tm_wday}\n"
    time.sleep(2)
    print("Connecting...")
    ser = serial.Serial(port=comport, baudrate=115200, timeout=1)
    time.sleep(2)  # Wait for the connection to stabilize
    get_REPL()
    command = "import menu"
    ser.write(command.encode('utf-8')) 
    ser.write(b'\x04')  # Ctrl+D triggers compilation and execution
    time.sleep(1)
    ser.write(time_string.encode('utf-8'))
    print(f"Successfully sent time to ESP32: {time_string.strip()}")

    while True:
        response = ser.readline().decode('utf-8').strip() # Read response
        if response:
            print(f"ESP32S3 response: {response}")
            if response == "Note":
                print("Note selected")
                subprocess.run(["notepad.exe"])
            if response == "Term":
                subprocess.Popen("start cmd /k echo Hello World", shell=True)
            if response == "Calc":
                subprocess.run(["calc.exe"])

except Exception as e:
    print(f"Error: {e}")
    get_REPL()
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()