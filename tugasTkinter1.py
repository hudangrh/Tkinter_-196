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
mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Geografi",
    "Sejarah",
    "Informatika"
]
frame_input = tk.Frame(frame, bg="white")
frame_input.pack(fill="x")

entries = []

for i, mapel in enumerate(mata_pelajaran):
    label = tk.Label(
        frame_input,
        text=f"Nilai {mapel}",
        font=("Arial", 10),
        bg="white",
        anchor="w",
        width=18
    )
    label.grid(row=i, column=0, sticky="w", pady=5)

    entry = ttk.Entry(frame_input, width=20)
    entry.grid(row=i, column=1, padx=(10, 0), pady=5)

    entries.append(entry)

tombol_prediksi = tk.Button(
    frame,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 11, "bold"),
    bg="#1d72b8",
    fg="white",
    activebackground="#155a8a",
    activeforeground="white",
    cursor="hand2",
    width=20,
    pady=8
)
tombol_prediksi.pack(pady=20)
label_hasil = tk.Label(
    frame,
    text="Hasil Prediksi: -",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#16803c",
    wraplength=400