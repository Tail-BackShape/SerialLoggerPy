import tkinter as tk

def process_number(number):
    print(f"Processing number: {number}")

def process_entry(entry_field):
    number = entry_field.get()
    if number.isdigit():
        process_number(int(number))
    else:
        print("Invalid input. Please enter a number.")

def main():
    window = tk.Tk()
    window.title("Number Processor")

    entry = tk.Entry(window)
    entry.pack()

    process_button = tk.Button(window, text="Process", command=lambda: process_entry(entry))
    process_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
