import tkinter as tk

# Function to draw a rectangle and print the coordinates
def draw_rect(event):
    global top_left_x, top_left_y

    canvas.delete("rect")  # Remove previous rectangle if it exists
    end_x, end_y = event.x, event.y
    canvas.create_rectangle(top_left_x, top_left_y, end_x, end_y, outline='red', tag="rect")
    print(f"Top-Left: ({top_left_x}, {top_left_y}), Bottom-Right: ({end_x}, {end_y})")

# Function to record the first click coordinates
def on_click(event):
    global top_left_x, top_left_y, drawing
    top_left_x, top_left_y = event.x, event.y
    canvas.bind('<B1-Motion>', draw_rect)  # Bind movement to draw rectangle

# Initialize global variables
top_left_x, top_left_y = 0, 0
drawing = False

# Create the main window
root = tk.Tk()
root.attributes("-alpha", 0.0)  # Set the transparency of the window frame

# Remove window decorations
root.overrideredirect(True)

# Maximize the window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Fullscreen canvas with slight visibility to see what you're drawing
canvas = tk.Canvas(root, cursor='cross', bg='grey', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.configure(bg='systemTransparent')

# Bind the click event to start drawing
canvas.bind('<Button-1>', on_click)

# Escape to close
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
