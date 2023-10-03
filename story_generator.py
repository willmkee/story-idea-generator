import tkinter as tk
import random

def generate_story():
    favorite_works = open("favorites.txt").read().splitlines()
    story_parts = random.sample(favorite_works, 4)

    genre_label.config(text='Use the genre of ' + story_parts[0])
    plot_label.config(text='Use the plot of ' + story_parts[1])
    characters_label.config(text='Use the characters from ' + story_parts[2])
    theme_label.config(text='Use the theme of ' + story_parts[3])

# Create the main application window and set its size
root = tk.Tk()
root.title("Story Generator")
root.geometry("400x300")  # Set the initial window size

# Create and configure labels
genre_label = tk.Label(root, text='', wraplength=300)
plot_label = tk.Label(root, text='', wraplength=300)
characters_label = tk.Label(root, text='', wraplength=300)
theme_label = tk.Label(root, text='', wraplength=300)

# Create a Generate button with padding
generate_button = tk.Button(root, text="Generate Story", command=generate_story, padx=10, pady=10)

# Use grid to center the button and labels
genre_label.grid(row=0, column=0, columnspan=2)
plot_label.grid(row=1, column=0, columnspan=2)
characters_label.grid(row=2, column=0, columnspan=2)
theme_label.grid(row=3, column=0, columnspan=2)
generate_button.grid(row=4, column=0, columnspan=2)

# Configure column and row weights to center the content
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

# Start the GUI application
root.mainloop()
