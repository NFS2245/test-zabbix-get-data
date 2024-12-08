from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Label, Entry, Frame, Progressbar
from tkinter import filedialog, Text, Scrollbar, messagebox
from threading import Thread
from data_processing import process_data, check_internet_connection, setup_logging

def build_ui(root):
    """Fungsi untuk membangun antarmuka pengguna."""
    style = Style(theme="superhero")

    # Setup logging
    setup_logging()

    # Menonaktifkan kemampuan untuk memaksimalkan jendela
    root.resizable(False, False)

    # --- Frame Input/Output ---
    frame_io = Frame(root, padding=10)
    frame_io.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    Label(frame_io, text="File Input:").grid(row=0, column=0, padx=10, pady=5)
    input_entry = Entry(frame_io, width=50)
    input_entry.grid(row=0, column=1, padx=10, pady=5)
    Button(frame_io, text="Browse", command=lambda: select_file(input_entry)).grid(row=0, column=2, padx=10, pady=5)

    Label(frame_io, text="Folder Output:").grid(row=1, column=0, padx=10, pady=5)
    output_entry = Entry(frame_io, width=50)
    output_entry.grid(row=1, column=1, padx=10, pady=5)
    Button(frame_io, text="Browse", command=lambda: select_folder(output_entry)).grid(row=1, column=2, padx=10, pady=5)

    # --- Frame Progress ---
    frame_progress = Frame(root, padding=10)
    frame_progress.grid(row=1, column=0, columnspan=3)

    progress_bar = Progressbar(frame_progress, orient="horizontal", length=400, mode="determinate")
    progress_bar.grid(row=0, column=0, columnspan=3, pady=5)

    progress_label = Label(frame_progress, text="")
    progress_label.grid(row=1, column=0, columnspan=3)

    # --- Frame Log ---
    frame_log = Frame(root, padding=10)
    frame_log.grid(row=2, column=0, columnspan=3)

    Label(frame_log, text="Log Output:").grid(row=0, column=0, columnspan=3)
    terminal = Text(frame_log, height=15, width=70)
    terminal.grid(row=1, column=0, columnspan=3)
    scrollbar = Scrollbar(frame_log, command=terminal.yview)
    scrollbar.grid(row=1, column=3, sticky="ns")
    terminal.config(yscrollcommand=scrollbar.set)

    Button(frame_io, text="Run", command=lambda: run_processing(input_entry, output_entry, progress_bar, progress_label, terminal)).grid(row=2, column=0, columnspan=3, pady=10)

def select_file(entry):
    """Fungsi untuk memilih file input."""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    entry.delete(0, "end")
    entry.insert(0, file_path)

def select_folder(entry):
    """Fungsi untuk memilih folder output."""
    folder_path = filedialog.askdirectory()
    entry.delete(0, "end")
    entry.insert(0, folder_path)

def run_processing(input_entry, output_entry, progress_bar, progress_label, terminal):
    """Fungsi untuk menjalankan proses pengolahan data."""
    input_path = input_entry.get()
    output_folder = output_entry.get()

    if not check_internet_connection():
        messagebox.showerror("Error", "Tidak ada koneksi internet.")
        return

    if not input_path or not output_folder:
        messagebox.showerror("Error", "Lengkapi file input dan folder output.")
        return

    # Menjalankan proses pengolahan data di thread terpisah
    Thread(target=lambda: process_data(input_path, output_folder, progress_bar, progress_label, terminal)).start()
