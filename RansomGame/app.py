import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import time

# Main Menu
def main_menu():
    """Create the main menu for the game."""
    def start_game():
        """Start the quiz game."""
        menu_window.destroy()  # Close the menu window
        quiz_game()  # Start the quiz game

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
    menu_window.overrideredirect(True)  # Remove window border
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

    # Load and place technion logo as .png in the top-right corner (transparent background)
    technion_logo = Image.open("technion-logo.png").convert("RGBA")  # Use PNG with transparent background
    technion_logo = technion_logo.resize((128, 128), Image.Resampling.LANCZOS)  # Resize for proper display
    technion_logo_photo = ImageTk.PhotoImage(technion_logo)

    # Load and place akm logo as .ico to the left of the technion logo
    akm_logo = Image.open("akm-logo.ico").convert("RGBA")  # Use .ico file with transparency
    akm_logo = akm_logo.resize((128, 128), Image.Resampling.LANCZOS)  # Resize to match technion logo
    akm_logo_photo = ImageTk.PhotoImage(akm_logo)

    canvas.create_image(screen_width - 300, 20, image=akm_logo_photo, anchor="nw")
    canvas.create_image(screen_width - 150, 20, image=technion_logo_photo, anchor="nw")

    # Game Title
    canvas.create_text(40, 50, text="BambooRansom", font=("Arial", 32, "bold"), fill="white", anchor="w")

    # Start Game Button
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 150,
        y=screen_height // 2 - 100,
        width=300,
        height=60,
        text="Start Game",
        command=start_game,
    )

    # Instructions Button
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 150,
        y=screen_height // 2,
        width=300,
        height=60,
        text="Instructions",
        command=show_instructions,
    )

    # Exit Button
    create_futuristic_button(
        canvas=canvas,
        x=screen_width // 2 - 150,
        y=screen_height // 2 + 100,
        width=300,
        height=60,
        text="Exit",
        command=exit_game,
    )

    # Keep references to avoid garbage collection
    canvas.image = bg_photo
    canvas.technion_logo_photo = technion_logo_photo  # Keep a reference to the technion logo image
    canvas.akm_logo_photo = akm_logo_photo  # Keep a reference to the akm logo image

    menu_window.mainloop()

# Quiz Game
def quiz_game():
    """Start the quiz game."""
    global current_question, score, max_score_per_question, questions
    current_question = 0
    score = 0
    max_score_per_question = 1000

    questions = [
        {
            "question": "What is the most common form of cyber attack?",
            "options": ["Phishing", "DDoS Attack", "Ransomware", "SQL Injection"],
            "correct": 0,
        },
        {
            "question": "Which protocol is used to encrypt web traffic?",
            "options": ["HTTP", "SSL/TLS", "FTP", "SMTP"],
            "correct": 1,
        },
        {
            "question": "What is the primary goal of a firewall?",
            "options": ["Prevent virus attacks", "Control network traffic", "Encrypt data", "Monitor CPU usage"],
            "correct": 1,
        },
    ]

    def start_timer(seconds):
        global timer_running, time_left
        timer_running = True
        time_left = seconds
        for i in range(seconds, -1, -1):
            if not timer_running:
                break
            time_left = i
            timer_canvas.delete("timer")
            timer_canvas.create_oval(20, 20, 180, 180, outline="white", width=5)
            timer_canvas.create_text(100, 100, text=str(i), font=("Arial", 32), fill="white", tags="timer")
            time.sleep(1)

        if timer_running:
            timer_running = False
            check_answer(-1)

    def start_timer_thread(seconds=20):
        threading.Thread(target=start_timer, args=(seconds,), daemon=True).start()

    def display_question():
        global selected_option, timer_running, points_earned

        selected_option = -1
        question_label.config(text=questions[current_question]["question"])

        for i, option in enumerate(questions[current_question]["options"]):
            option_buttons[i].config(text=option, state="normal", bg=option_colors[i])

        feedback_label.config(text="")
        next_button.config(state="disabled")
        points_earned = max_score_per_question

        timer_running = False
        start_timer_thread(20)

    def select_option(idx):
        global selected_option

        selected_option = idx

        for i, button in enumerate(option_buttons):
            if i == idx:
                button.config(bg="#28a745")
            else:
                button.config(bg=option_colors[i])

        next_button.config(state="normal")

    def check_answer(selected_idx):
        global current_question, score, points_earned, timer_running

        timer_running = False
        correct_option = questions[current_question]["correct"]

        if selected_idx == correct_option:
            points_earned = int(max_score_per_question * (time_left / 20))
            score += points_earned
            feedback_label.config(text=f"✅ Correct! You earned {points_earned} points.", fg="green")
        elif selected_idx == -1:
            points_earned = 0
            feedback_label.config(text="⏰ Time's up! No answer selected.", fg="red")
        else:
            points_earned = 0
            feedback_label.config(
                text=f"❌ Incorrect! Correct: {questions[current_question]['options'][correct_option]}.",
                fg="red",
            )

        for btn in option_buttons:
            btn.config(state="disabled")

        current_question += 1
        if current_question < len(questions):
            window.after(1500, display_question)
        else:
            window.after(1500, show_score)

    def show_score():
        messagebox.showinfo("Quiz Completed", f"Your final score is: {score}/{len(questions) * max_score_per_question}")
        window.destroy()

    window = tk.Tk()
    window.title("Cybersecurity Quiz")
    window.geometry("800x600")
    window.configure(bg="black")

    question_label = tk.Label(window, text="", font=("Arial", 18), bg="black", fg="white", wraplength=700, justify="center")
    question_label.pack(pady=20)

    timer_canvas = tk.Canvas(window, width=200, height=200, bg="black", highlightthickness=0)
    timer_canvas.pack()

    options_frame = tk.Frame(window, bg="black")
    options_frame.pack(pady=50)

    option_colors = ["#003366", "#8B0000", "#006400", "#FFD700"]
    option_buttons = []
    for i in range(4):
        btn = tk.Button(
            options_frame,
            text="",
            font=("Arial", 16),
            bg=option_colors[i],
            fg="white",
            width=40,
            height=2,
            relief="solid",
            command=lambda idx=i: select_option(idx),
        )
        row = i // 2
        col = i % 2
        btn.grid(row=row, column=col, padx=20, pady=10)
        option_buttons.append(btn)

    feedback_label = tk.Label(window, text="", font=("Arial", 14), bg="black", fg="lime")
    feedback_label.pack(pady=10)

    next_button = tk.Button(
        window,
        text="Next",
        font=("Arial", 14),
        bg="gray",
        fg="white",
        width=20,
        state="disabled",
        command=lambda: check_answer(selected_option),
    )
    next_button.pack(pady=20)

    display_question()
    window.mainloop()

if __name__ == "__main__":
    main_menu()
