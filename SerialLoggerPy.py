import serial
from datetime import datetime

def main():

    filename = input("Enter filename: ")
    f = open("./log/" + filename + ".txt","w+")

    try:
        COMPort = input("Enter COM Port: ")
        ser = serial.Serial(COMPort, 9600)

        while True:
            now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S, ")
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
