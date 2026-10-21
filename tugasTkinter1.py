import tkinter as tk
from tkinter import ttk

def hasil_prediksi():
    label_hasil.config(text="Hasil Prediksi: TeknologiInformasi")
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.resizable(False, False)
root.configure(bg="#f0f4f8")
frame = tk.Frame(root, bg="white", padx=30, pady=25)
frame.pack(padx=20, pady=20, fill="both", expand=True)
Label = tk.Label(
    frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#1d3557"
)
Label.pack(pady=10)