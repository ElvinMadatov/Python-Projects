import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import options  # Importing the options file for the new screen

# Main Menu
def main_menu():
    """Create the main menu for the game."""
    def start_game():
        """Start the game screen with new buttons."""
        menu_window.destroy()  # Close the menu window
        options.game_screen()  # Start the new screen from options.py

    def show_instructions():
        """Show instructions for the game."""
        messagebox.showinfo(
            "Instructions",
            "Welcome to the Cybersecurity Quiz!\n\n"
            "1. Each question has 4 options.\n"
            "2. You earn points based on how quickly you answer.\n"
            "3. Max score per question is 1000 points.\n"
            "4. Be quick but careful!\n\nGood luck!",
        )

    def exit_game():
        """Exit the game."""
        menu_window.destroy()

    def create_futuristic_button(canvas, x, y, width, height, text, command):
        """Create a futuristic button with hover effects."""
        def on_click(event):
            command()

        def on_enter(event):
            canvas.itemconfig(button_rect, fill="#00FFFF")  # Hover color
            canvas.itemconfig(button_text, fill="#000000")

        def on_leave(event):
            canvas.itemconfig(button_rect, fill="#002244")
            canvas.itemconfig(button_text, fill="#FFFFFF")

        button_rect = canvas.create_rectangle(
            x, y, x + width, y + height, outline="#00FFFF", width=2, fill="#002244"
        )

        button_text = canvas.create_text(
            x + width / 2, y + height / 2, text=text, font=("Arial", 20, "bold"), fill="#FFFFFF"
        )

        canvas.tag_bind(button_rect, "<Button-1>", on_click)
        canvas.tag_bind(button_rect, "<Enter>", on_enter)
        canvas.tag_bind(button_rect, "<Leave>", on_leave)
        canvas.tag_bind(button_text, "<Button-1>", on_click)
        canvas.tag_bind(button_text, "<Enter>", on_enter)
        canvas.tag_bind(button_text, "<Leave>", on_leave)

    # Create the main menu window
    menu_window = tk.Tk()
    menu_window.geometry(f"{menu_window.winfo_screenwidth()}x{menu_window.winfo_screenheight()}+0+0")
    menu_window.configure(bg="white")
    menu_window.title("Cybersecurity Quiz - Menu")

    # Get screen dimensions
    screen_width = menu_window.winfo_screenwidth()
    screen_height = menu_window.winfo_screenheight()

    # Load background image using Pillow
    bg_image = Image.open("encrypt.jpg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Add background image to the window using Canvas
    canvas = tk.Canvas(menu_window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Load salam.png image using Pillow (Resizing with increased width)
    salam_image = Image.open("salam.png")
    salam_image = salam_image.resize((320, 180), Image.Resampling.LANCZOS)  # Increased width and adjusted height
    salam_photo = ImageTk.PhotoImage(salam_image)

    # Add salam.png to the top-right corner with some separation
    canvas.create_image(screen_width - 20, 20, image=salam_photo, anchor="ne")

    # Game Title
    canvas.create_text(40, 50, text="BambooRansom", font=("Arial", 32, "bold"), fill="white", anchor="w")

    # Start Game Button
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 820,
        y=screen_height // 2 - 120,
        width=300,
        height=60,
        text="Start Game",
        command=start_game,
    )

    # Instructions Button
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 820,
        y=screen_height // 2 - 10,
        width=300,
        height=60,
        text="Instructions",
        command=show_instructions,
    )

    # Exit Button
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 820,
        y=screen_height // 2 + 100,
        width=300,
        height=60,
        text="Exit",
        command=exit_game,
    )

    # Start the main event loop
    menu_window.mainloop()

if __name__ == "__main__":
    main_menu()
