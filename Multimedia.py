import tkinter as tk
from tkinter import messagebox, ttk
from gtts import gTTS
import subprocess
import platform

# Define supported languages and their flag colors
SUPPORTED_LANGUAGES = {
    "English": {"code": "en", "color": "#1abc9c"},  # Teal for English
    "Arabic": {"code": "ar", "color": "#e74c3c"},  # Red for Arabic
    "French": {"code": "fr", "color": "#3498db"},  # Blue for French
    "Spanish": {"code": "es", "color": "#f39c12"},  # Orange for Spanish
}

# Define global variables
selected_color = "#ffffff"  # Default text color


def play_text():
    """Convert text to speech and play the audio."""
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            language = SUPPORTED_LANGUAGES.get(lang_var.get(), {"code": "en"})["code"]
            tts = gTTS(text, lang=language)
            audio_file = "output.mp3"
            tts.save(audio_file)

            # Platform-independent audio playback
            if platform.system() == "Windows":
                subprocess.run(["start", audio_file], shell=True)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["afplay", audio_file])
            else:  # Linux/Other
                subprocess.run(["xdg-open", audio_file])
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")


def clear_text():
    """Clear the text entry."""
    text_entry.delete("1.0", tk.END)


def exit_app():
    """Exit the application."""
    root.destroy()


def change_text_color(event):
    """Change the text color based on the selected language."""
    global selected_color
    language = lang_var.get()
    selected_color = SUPPORTED_LANGUAGES.get(language, {}).get("color", "#ffffff")
    text_entry.config(fg=selected_color)


# Create the main window
root = tk.Tk()
root.title("Modern Text-to-Speech App")
root.geometry("800x600")  # Wider size
root.resizable(True, True)  # Enable resizing
root.configure(bg="#000000")  # Black background for a modern look

# Header
header = tk.Label(
    root,
    text="🗣️ Modern Text-to-Speech 🌟",
    font=("Arial", 24, "bold"),
    bg="#000000",
    fg="#00cec9"  # Light teal text
)
header.pack(pady=20)

# Language selection
lang_var = tk.StringVar(value="English")
lang_frame = tk.Frame(root, bg="#000000")
lang_frame.pack(pady=10)

lang_label = tk.Label(
    lang_frame,
    text="🌐 Select Language:",
    font=("Arial", 14),
    bg="#000000",
    fg="#ffffff"
)
lang_label.pack(side=tk.LEFT, padx=10)

lang_menu = ttk.Combobox(
    lang_frame,
    textvariable=lang_var,
    values=list(SUPPORTED_LANGUAGES.keys()),
    state="readonly",
    width=15,
    font=("Arial", 12)
)
lang_menu.pack(side=tk.LEFT, padx=10)
lang_menu.bind("<<ComboboxSelected>>", change_text_color)

# Text entry
text_frame = tk.Frame(root, bg="#1c1c1c", bd=2, relief="ridge")
text_frame.pack(padx=20, pady=20, fill=tk.BOTH)

text_label = tk.Label(
    text_frame,
    text="📝 Enter Your Text Here:",
    font=("Arial", 12, "bold"),
    bg="#1c1c1c",
    fg="#ecf0f1"
)
text_label.pack(anchor="w", padx=10, pady=5)

text_entry = tk.Text(
    text_frame,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#2c2c2c",  # Darker gray background for the text box
    fg="#ffffff",
    height=6,  # Smaller height
    insertbackground="#1abc9c",  # Teal cursor
)
text_entry.pack(padx=10, pady=10, fill=tk.BOTH)

# Buttons
button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(pady=20)

play_button = tk.Button(
    button_frame,
    text="▶ Play",
    command=play_text,
    font=("Arial", 14, "bold"),
    bg="#1abc9c",  # Teal button
    fg="#ffffff",
    activebackground="#16a085",
    activeforeground="#ffffff",
    relief="flat",
    width=10
)
play_button.grid(row=0, column=0, padx=15)

clear_button = tk.Button(
    button_frame,
    text="🧹 Set",
    command=clear_text,
    font=("Arial", 14, "bold"),
    bg="#f39c12",  # Orange button
    fg="#ffffff",
    activebackground="#d35400",
    activeforeground="#ffffff",
    relief="flat",
    width=10
)
clear_button.grid(row=0, column=1, padx=15)

exit_button = tk.Button(
    button_frame,
    text="❌ Exit",
    command=exit_app,
    font=("Arial", 14, "bold"),
    bg="#e74c3c",  # Red button
    fg="#ffffff",
    activebackground="#c0392b",
    activeforeground="#ffffff",
    relief="flat",
    width=10
)
exit_button.grid(row=0, column=2, padx=15)

# Footer
footer = tk.Label(
    root,
    text="© 2024 Developed by Mohamed Elsayed Eleshmawi",
    font=("Arial", 10, "italic"),
    bg="#000000",
    fg="#7f8c8d"
)
footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
