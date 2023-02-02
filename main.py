import tkinter as tk
from tkinter import messagebox
import time
import random
from PIL import Image, ImageTk

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")
        #self.master.geometry("740x444")
        self.master.geometry("886x532")
        self.master.resizable(False, False)        
        sentences = [
            "The quick brown fox jumps over the lazy dog",
            "The five boxing wizards jump quickly",
            "Pack my box with five dozen liquor jugs",
            "Waxy and quivering, jocks fumble the pizza.",
            "The best preparation for tomorrow is doing your best today.",
            "Life is a journey, not a destination.",
            "A quick witted jester can make a dull king laugh with joy."
            ]
        self.text = random.choice(sentences)
        self._create_widgets()

    def _create_widgets(self):
        background_image = Image.open("image.jpg")
        background_image = background_image.resize((886, 532), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self.master, image=background_image)
        self.background_label.image = background_image
        self.background_label.pack(fill="both", expand=True)
        self.text_label = tk.Label(self.background_label, text=self.text, font=("KaiTi", 20),fg="#fbf4fb",bg="#1f2025",justify="center")
        self.text_label.pack(pady=150)
        self.text_entry = tk.Entry(self.background_label, font=("KaiTi", 20),bg="#263747",fg="#d9dfeb",justify="center")
        self.text_entry.pack(pady=0)
        self.text_entry.focus_set()
        self.text_entry.bind("<Return>", self._check_typing)
        self.check_button = tk.Button(self.background_label, text="Check", command=self._check_typing, font=("KaiTi", 20),bg="#bbc5ce")
        self.check_button.pack(pady=0)
        self.time_label = tk.Label(self.background_label)
        self.time_label.pack()
        self.start_time = time.time()
        self.elapsed_time = 0
    
    def _check_typing(self, event=None):
        self.elapsed_time = time.time() - self.start_time
        self.time_label.config(text=f"{round(self.elapsed_time, 2)} seconds")
        typed_text = self.text_entry.get()
        wpm = self._calculate_wpm(typed_text)
        if typed_text == self.text:
            messagebox.showinfo("Result", f"You typed {wpm} WPM in {round(self.elapsed_time, 2)} seconds")
            self.master.destroy()
            root = tk.Tk()
            app = TypingSpeedTest(root)
            root.mainloop()
        else:
            mistakes = [t for i,t in enumerate(typed_text.split()) if t != self.text.split()[i]]
            messagebox.showwarning("Result", f"You typed {wpm} WPM in {round(self.elapsed_time, 2)} seconds\nMistakes: {mistakes}")
            self.text_entry.delete(0, tk.END)
            self._create_widgets()
            self.master.destroy()
            root = tk.Tk()
            app = TypingSpeedTest(root)
            root.mainloop()
    def _calculate_wpm(self, typed_text):
        typed_word_count = len(typed_text.split())
        wpm = round(typed_word_count / (self.elapsed_time / 60))
        return wpm

if __name__ == "__main__":
	root = tk.Tk()
	TypingSpeedTest(root)
	root.mainloop()

