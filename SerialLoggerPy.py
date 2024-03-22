import tkinter as tk
import serial
import serial.tools.list_ports
import threading
from datetime import datetime

def serial_writer(ser, writedata):
    ser.write((str(writedata) + "\r\n").encode('utf-8'))

def write_entry(entry_field, ser):
    writedata = entry_field.get()
    serial_writer(ser, writedata)  # 文字列として直接シリアルに送信
    entry_field.delete(0, tk.END)

def read_serial(ser, f):
    while ser.isOpen():
        now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f,")
        data = (ser.readline()).decode('utf-8')
        print(now, data.strip())
        f.write(now + data.strip() + "\n")

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
        thread = threading.Thread(target=read_serial, args=(ser, f))
        thread.start()

        window = tk.Tk()
        window.title("Serial writer")

        entry = tk.Entry(window)
        entry.pack()

        write_button = tk.Button(window, text="Write", command=lambda: write_entry(entry, ser))
        write_button.pack()

        window.mainloop()

    except KeyboardInterrupt:
        ser.close()
        f.close()

    finally:
        ser.close()
        f.close()

if __name__ == "__main__":
    main()
