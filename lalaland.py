import tkinter as tk
from tkinter import messagebox, ttk
from gtts import gTTS
import playsound
import os

root = tk.Tk()
root.title("Text to Speech / تحويل النص إلى كلام")
root.geometry("600x500")
root.configure(bg="black")

mylabel = tk.Label(root, text="Text to Speech / تحويل النص إلى كلام", font=("Arial", 16, "bold"), bg="black", fg="white")
mylabel.pack(pady=20)

myentry = tk.Entry(root, width=40, font=("Arial", 14), bd=2, bg="white", fg="black")
myentry.pack(pady=10, padx=20)

language_var = tk.StringVar(value='English')
lang_label = tk.Label(root, text="Select Language / اختر اللغة:", font=("Arial", 12), bg="black", fg="white")
lang_label.pack(pady=10)

lang_selector = ttk.Combobox(root, textvariable=language_var)
lang_selector['values'] = ('English', 'العربية')
lang_selector.pack(pady=5, padx=20)

progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
progress_bar.pack(pady=20)

def text_to_speech():
    text = myentry.get()
    if text.strip():
        progress_bar.start(10)
        audio_file = f"speech_{int(os.times().system)}.mp3"
        try:
            lang = 'en' if language_var.get() == 'English' else 'ar'
            tts = gTTS(text=text, lang=lang)
            tts.save(audio_file)
            playsound.playsound(audio_file)
        except Exception as e:
            messagebox.showerror("Error / خطأ", f"An error occurred: {str(e)}")
        finally:
            progress_bar.stop()
            if os.path.exists(audio_file):
                os.remove(audio_file)
    else:
        messagebox.showwarning("Input Error / خطأ في الإدخال", "Please enter text to convert. / يرجى إدخال نص للتحويل.")

myframe = tk.Frame(root, bg="black")
myframe.pack(side=tk.BOTTOM, pady=30)

play_button = tk.Button(myframe, text="Play / تشغيل", command=text_to_speech, bg="green", fg="white", width=12, height=2)
play_button.grid(row=0, column=0, padx=20)

set_button = tk.Button(myframe, text="Set / مسح", command=lambda: myentry.delete(0, tk.END), bg="blue", fg="white", width=12, height=2)
set_button.grid(row=0, column=1, padx=20)

exit_button = tk.Button(myframe, text="Exit / خروج", command=root.destroy, bg="red", fg="white", width=12, height=2)
exit_button.grid(row=0, column=2, padx=20)

root.mainloop()