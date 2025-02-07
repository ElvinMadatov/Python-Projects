from PIL import Image, ImageTk
import tkinter as tk
import quiz  # Assuming this is where your quiz logic is stored

def show_warning():
    """Create a warning screen with a centered message and a start button."""
    # Yeni bir pencere oluştur
    window = tk.Toplevel()  # Ana pencerenin üstünde yeni bir pencere
    window.title("Warning Screen")

    # Pencere boyutunu ekran boyutuna ayarla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")

    # Arka plan resmi yükle
    bg_image = Image.open("encrypt.jpg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Canvas oluştur ve resmi yerleştir
    canvas = tk.Canvas(window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # İlk metin: "Pay attention"
    canvas.create_text(
        screen_width // 2,
        screen_height // 2 - 50,
        text="Pay Attention",
        font=("Arial", 36, "bold"),
        fill="white"
    )

    # İkinci metin: "Eğer sen ilk level 3 sehv etsen sekiller faylin sifrelenecek"
    canvas.create_text(
        screen_width // 2,
        screen_height // 2 + 20,
        text="If you make the first level 3 mistakes, the image file will be encrypted.",
        font=("Arial", 24),
        fill="white"
    )

    # Buton ekle
    def start_quiz():
        """Function to start the quiz when the button is clicked."""
        # Close the warning window
        window.destroy()
        # Assuming 'quiz' has a function to start the quiz, call it here
        quiz.quiz_screen()

    start_button = tk.Button(
        window, text="Start Quiz", font=("Arial", 20), command=start_quiz, bg="green", fg="white"
    )
    start_button.place(relx=0.5, rely=0.7, anchor="center")  # Position the button in the center

    window.mainloop()

# Example usage: show_warning() can be called to display the warning screen
