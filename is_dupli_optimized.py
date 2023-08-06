# class Solution:
#     def containsDuplicate(self, nums):
#         x = set(nums)
#         l1 = len(nums)
#         l2 = len(x)

#         if l1 != l2:
#             return True
#         else:
#             return False 

import tkinter as tk

# Function to handle button clicks
def button_click(event):
    # Get the clicked button's text
    button_text = event.widget.cget("text")

    if button_text == "=":
        # Evaluate the expression
        try:
            result = eval(display.get())
            display.set(result)
        except:
            display.set("Error")

    elif button_text == "C":
        # Clear the display
        display.set("")

    else:
        # Append the clicked button's text to the display
        display.set(display.get() + button_text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Define colors
button_bg = "#F0F0F0"  # Light gray
button_fg = "#000000"  # Black
display_bg = "#FFFFFF"  # White
display_fg = "#000000"  # Black

# Create the display widget
display = tk.StringVar()
display_entry = tk.Entry(window, textvariable=display, font=("Arial", 20), justify="right",
                         bg=display_bg, fg=display_fg)
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
col = 0
for button in buttons:
    button_widget = tk.Button(window, text=button, font=("Arial", 15), padx=15, pady=10,
                             bg=button_bg, fg=button_fg)
    button_widget.grid(row=row, column=col, padx=5, pady=5)
    button_widget.bind("<Button-1>", button_click)  # Bind left mouse button click event
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main event loop
window.mainloop()
