import serial

def main():
    try:
        COMPort = input("Enter COM Port: ")
        ser = serial.Serial(COMPort, 9600)

        while True:
            data = ser.readline()
            print(data.decode('utf-8').strip())

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()
