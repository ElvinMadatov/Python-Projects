import tkinter as tk
from PIL import Image, ImageTk
import warning  # Import the warning screen when a button is clicked

def game_screen():
    """Create a new screen with 3 options."""
    def select_option(option):
        """Handle option selection and open the warning screen."""
        print(f"Selected: {option}")
        warning.show_warning()  # Open the warning screen when an option is selected

    # Create the game window
    game_window = tk.Tk()
    game_window.title("Game Options")
    
    # Set the window size to match the first page
    game_window.geometry(f"{game_window.winfo_screenwidth()}x{game_window.winfo_screenheight()}+0+0")
    game_window.configure(bg="white")

    # Get screen dimensions
    screen_width = game_window.winfo_screenwidth()
    screen_height = game_window.winfo_screenheight()

    # Load background image using Pillow (same as main menu)
    bg_image = Image.open("encrypt.jpg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create canvas for the background image
    canvas = tk.Canvas(game_window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Load salam.png image using Pillow (Resizing with increased width)
    salam_image = Image.open("salam.png")
    salam_image = salam_image.resize((320, 180), Image.Resampling.LANCZOS)  # Increased width and adjusted height
    salam_photo = ImageTk.PhotoImage(salam_image)

    # Add salam.png to the top-right corner with some separation
    canvas.create_image(screen_width - 20, 20, image=salam_photo, anchor="ne")

    # Game Title (same font and color)
    canvas.create_text(40, 50, text="Choose your field", font=("Arial", 32, "bold"), fill="white", anchor="w")

    # Create 3 options buttons (Red, Blue, Essential) with the same style as the first screen
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 820,
        y=screen_height // 2 - 120,
        width=300,
        height=60,
        text="Red",
        command=lambda: select_option("Red"),
    )
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 820,
        y=screen_height // 2 - 10,
        width=300,
        height=60,
        text="Blue",
        command=lambda: select_option("Blue"),
    )
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 820,
        y=screen_height // 2 + 100,
        width=300,
        height=60,
        text="Essential",
        command=lambda: select_option("Essential"),
    )

    # Keep references to avoid garbage collection
    canvas.image = bg_photo  # Keep a reference to the background image

    # Start the game screen event loop
    game_window.mainloop()

def create_futuristic_button(canvas, x, y, width, height, text, command):
    """Create a futuristic button with hover effects."""
    def on_click(event):
        command()

    def on_enter(event):
        canvas.itemconfig(button_rect, fill="#00FFFF")  # Hover color
        canvas.itemconfig(button_text, fill="#000000")

    def on_leave(event):
        canvas.itemconfig(button_rect, fill="#002244")  # Default color
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
