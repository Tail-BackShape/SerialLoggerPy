import serial

def main():

    filename = input("Enter filename: ")
    f = open("./log/" + filename + ".txt","w+")

    try:
        COMPort = input("Enter COM Port: ")
        ser = serial.Serial(COMPort, 9600)

        while True:
            data = (ser.readline()).decode('utf-8')
            print(data.strip())
            f.write(data.strip() + "\n")

    # Close serial port on keyboard interrupt
    except KeyboardInterrupt:
        ser.close()
        f.close()

if __name__ == "__main__":
    main()
