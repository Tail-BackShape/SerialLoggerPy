import tkinter as tk
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
            window = tk.Tk()
            window.title("Serial writer")

            entry = tk.Entry(window)
            entry.pack()

            write_button = tk.Button(window, text="Write", command=lambda: write_entry(entry))
            write_button.pack()

            def serial_writer(writedata):
                ser.write((writedata + "\r\n").encode('utf-8'))

            def write_entry(entry_field):
                writedata = entry_field.get()
                if writedata.isdigit():
                    serial_writer(int(writedata))


            now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f,")
            data = (ser.readline()).decode('utf-8')
            print(now, data.strip())
            f.write(now)
            f.write(data.strip() + "\n")

            window.mainloop()

    # Close serial port on keyboard interrupt
    except KeyboardInterrupt:
        ser.close()
        f.close()

    finally:
        ser.close()
        f.close()

if __name__ == "__main__":
    main()
