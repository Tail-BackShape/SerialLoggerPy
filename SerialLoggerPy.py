import serial
import serial.tools.list_ports

from datetime import datetime

def main():

    filename = input("Enter filename: ")
    f = open("./log/" + filename + ".txt","w+")

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)

    COMPort = input("Enter COM Port: ")

    try:

        ser = serial.Serial(COMPort, 9600)

        while True:
            now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S,")
            data = (ser.readline()).decode('utf-8')
            print(now, data.strip())
            f.write(now)
            f.write(data.strip() + "\n")

    # Close serial port on keyboard interrupt
    except KeyboardInterrupt:
        ser.close()
        f.close()

if __name__ == "__main__":
    main()
