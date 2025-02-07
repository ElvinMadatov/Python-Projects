from tkinter import Toplevel, Label
from PIL import Image, ImageTk
import tkinter as tk

# JSON tabanlı soru verisi
questions = [
    {
        "question": "What is the common port number used for SSH?",
        "options": ["22", "80", "443", "21"],
        "answer": "22"
    },
    {
        "question": "Which tool is commonly used for monitoring network traffic?",
        "options": ["Wireshark", "Metasploit", "Nmap", "Burp Suite"],
        "answer": "Wireshark"
    },
    {
        "question": "Which of the following is a strong password?",
        "options": ["password123", "123456", "qwerty", "3x@mpl3Str0ng!"],
        "answer": "3x@mpl3Str0ng!"
    },
    {
        "question": "What is the default port for HTTP?",
        "options": ["80", "443", "21", "22"],
        "answer": "80"
    },
    {
        "question": "What does the 'ping' command do?",
        "options": ["Tests network connectivity", "Checks system memory", "Updates software", "Resets the router"],
        "answer": "Tests network connectivity"
    },
    {
        "question": "Which protocol is used for secure communication over the internet?",
        "options": ["HTTP", "HTTPS", "FTP", "SMTP"],
        "answer": "HTTPS"
    },
    {
        "question": "Which of the following is a type of malware?",
        "options": ["Virus", "Router", "Firewall", "Browser"],
        "answer": "Virus"
    },
    {
        "question": "What is the full form of 'IP' in networking?",
        "options": ["Internet Protocol", "Internet Port", "Information Protocol", "Integrated Protocol"],
        "answer": "Internet Protocol"
    },
    {
        "question": "Which port number is used by HTTPS?",
        "options": ["80", "443", "21", "22"],
        "answer": "443"
    },
    {
        "question": "Which of the following is a type of phishing attack?",
        "options": ["Email Phishing", "Spam", "Firewall", "Antivirus"],
        "answer": "Email Phishing"
    }
]

def quiz_screen():
    current_question = 0
    score = 0
    time_left = 15  # 15 saniye için zamanlayıcı

    def next_question(selected_option=None):
        nonlocal current_question, score, time_left

        # Cevabı kontrol et
        if selected_option == questions[current_question]["answer"]:
            score += 1

        # Bir sonraki soruya geç
        current_question += 1
        time_left = 15  # Zamanı sıfırla

        if current_question < len(questions):
            load_question()
        else:
            # Tüm sorular bittiğinde sonucu göster
            canvas.delete("all")
            canvas.create_text(
                screen_width // 2,
                screen_height // 2,
                text=f"Quiz Finished! Your Score: {score}/{len(questions)}",
                font=("Arial", 36, "bold"),
                fill="white"
            )
            for button in option_buttons:
                button.destroy()

    def load_question():
        nonlocal time_left
        time_left = 15  # Her yeni soruda zamanlayıcıyı sıfırla

        # Soruyu ve seçenekleri güncelle
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])  # Soru metnini beyaz yapıyoruz
        for i, option in enumerate(question_data["options"]):
            option_buttons[i][0].config(  # Buton rect'ini güncelle
                text=option,
                command=lambda opt=option: next_question(opt)
            )
        update_timer()  # Timer başlat

    def update_timer():
        nonlocal time_left
        if time_left > 0:
            timer_label.config(text=f"Time Left: {time_left}s")
            time_left -= 1
            quiz_window.after(1000, update_timer)  # Zamanlayıcıyı 1 saniyede bir güncelle
        else:
            next_question()  # Zaman bittiğinde bir sonraki soruya geç

    # Quiz ekranını başlat
    quiz_window = Toplevel()
    quiz_window.title("Quiz Screen")
    screen_width = quiz_window.winfo_screenwidth()
    screen_height = quiz_window.winfo_screenheight()
    quiz_window.geometry(f"{screen_width}x{screen_height}+0+0")

    # Arka plan resmi
    bg_image = Image.open("encrypt.jpg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Canvas
    canvas = tk.Canvas(quiz_window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Resim referansını sakla (çöp toplanmasını önlemek için)
    canvas.image = bg_photo

    # Soru etiketi (Arka plan rengi yok)
    question_label = Label(quiz_window, text="", font=("Arial", 24, "bold"))
    question_label.place(relx=0.1, rely=0.2, anchor="w")  # Soru metni daha yüksek olacak şekilde yerleştirildi
    
    # Zamanlayıcı etiketi (Arka plan rengi yok)
    timer_label = Label(quiz_window, text="", font=("Arial", 20, "bold"))
    timer_label.place(relx=0.1, rely=0.1, anchor="w")  # Zamanlayıcı daha yüksek olacak şekilde yerleştirildi

    # Seçenek butonları (Yan yana)
    option_buttons = []
    button_positions = [
        (0.1, 0.4),  # Buton a (sol üst)
        (0.4, 0.4),  # Buton b (orta üst)
        (0.1, 0.6),  # Buton c (sol alt)
        (0.4, 0.6)   # Buton d (orta alt)
    ]

    # Main menu tarzı butonları oluştur
    for pos in button_positions:
        button_rect, button_text = create_futuristic_button(
            canvas=canvas,
            x=screen_width * pos[0],
            y=screen_height * pos[1],
            width=300,
            height=60,
            text="",  # Başlangıçta boş
            command=None  # Başlangıçta boş komut
        )
        option_buttons.append((button_rect, button_text))

    # İlk soruyu yükle
    load_question()

    quiz_window.mainloop()

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
        x + width / 2, y + height / 2, text=text, font=("Arial", 22, "bold"), fill="#FFFFFF"
    )

    canvas.tag_bind(button_rect, "<Button-1>", on_click)
    canvas.tag_bind(button_rect, "<Enter>", on_enter)
    canvas.tag_bind(button_rect, "<Leave>", on_leave)
    canvas.tag_bind(button_text, "<Button-1>", on_click)
    canvas.tag_bind(button_text, "<Enter>", on_enter)
    canvas.tag_bind(button_text, "<Leave>", on_leave)

    return button_rect, button_text  # return both rect and text references to avoid garbage collection
