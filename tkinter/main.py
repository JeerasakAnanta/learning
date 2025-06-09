import tkinter as tk


def on_click():
    label.config(text="You clicked me!")


def main():
    global label  # Make label accessible in on_click

    # Create the main window
    root = tk.Tk()
    root.title("Click Me App")

    label = tk.Label(root, text="Hello, click the button below!")
    label.pack(pady=10)

    button = tk.Button(root, text="Click Me", command=on_click)
    button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
