import serial
import serial.tools.list_ports

from datetime import datetime

def main():

    # Create a new file to log data
    filename = input("Enter filename: ")
    f = open("./log/" + filename + ".txt","w+")

    # List all available COM ports
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
    COMPort = input("Enter COM Port: ")

    # Baud rate specification
    baudRate = int(input("Enter Baud Rate(bps): "))

    try:

        ser = serial.Serial(COMPort, baudRate)

        while ser.isOpen():
            now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f,")
            data = (ser.readline()).decode('utf-8')
            print(now, data.strip())
            f.write(now)
            f.write(data.strip() + "\n")

    # Close serial port on keyboard interrupt
    except KeyboardInterrupt:
        ser.close()
        f.close()

    finally:
        ser.close()
        f.close()

if __name__ == "__main__":
    main()
