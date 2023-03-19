import os
from pdfminer.high_level import extract_text
from tkinter import filedialog, Tk, Label, Button, Text, Scrollbar, messagebox

def read_pdf_file(file_path):
    text = extract_text(file_path)
    return text

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        file_path_label.config(text=file_path)

def process_file():
    if not file_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    text = read_pdf_file(file_path)

    result_text.delete(1.0, "end")
    result_text.insert("end", f"Extracted Text:\n{text}\n")

def save_to_file():
    if not file_path:
        messagebox.showerror("Error", "Please process a PDF file first.")
        return

    text = result_text.get(1.0, "end-1c")

    save_file_path = filedialog.asksaveasfilename(initialdir=os.path.expanduser("~"), filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
    if save_file_path:
        with open(save_file_path, 'w', encoding='utf-8') as file:
            file.write(text)

root = Tk()
root.title("PDF to Text")
root.geometry("800x600")

file_path_label = Label(root, text="No file selected.", wraplength=800, font=("Helvetica", 14))
file_path_label.pack()

browse_button = Button(root, text="Browse PDF", command=browse_file, font=("Helvetica", 14), height=2, width=20)
browse_button.pack(pady=10)

process_button = Button(root, text="Process PDF", command=process_file, font=("Helvetica", 14), height=2, width=20)
process_button.pack(pady=10)

save_button = Button(root, text="Save to File", command=save_to_file, font=("Helvetica", 14), height=2, width=20)
save_button.pack(pady=10)

result_text = Text(root, wrap="word", height=15, font=("Helvetica", 14))
result_text.pack(pady=10)

scrollbar = Scrollbar(root, command=result_text.yview)
scrollbar.pack(side="right", fill="y")

result_text.config(yscrollcommand=scrollbar.set)

file_path = None

root.mainloop()
