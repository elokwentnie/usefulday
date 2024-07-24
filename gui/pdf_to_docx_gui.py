import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import parse

class PDFtoDOCXApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to DOCX Converter")
        self.root.geometry("400x200")
        
        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Input File
        self.input_file_label = tk.Label(self.root, text="Input PDF File:")
        self.input_file_label.pack(pady=10)
        
        self.input_file_entry = tk.Entry(self.root, width=50)
        self.input_file_entry.pack(pady=5)
        
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_input_file)
        self.browse_button.pack(pady=5)
        
        # Output File
        self.output_file_label = tk.Label(self.root, text="Output DOCX File (Optional):")
        self.output_file_label.pack(pady=10)
        
        self.output_file_entry = tk.Entry(self.root, width=50)
        self.output_file_entry.pack(pady=5)
        
        # Convert Button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_pdf_to_docx)
        self.convert_button.pack(pady=20)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(0, file_path)
    
    def convert_pdf_to_docx(self):
        input_file = self.input_file_entry.get()
        output_file = self.output_file_entry.get()
        
        if not input_file or not input_file.lower().endswith('.pdf'):
            messagebox.showerror("Error", "Please select a valid PDF file.")
            return
        
        if not output_file:
            output_file = input_file.rsplit(".", 1)[0] + ".docx"
        elif not output_file.lower().endswith('.docx'):
            messagebox.showerror("Error", "Output file must have a .docx extension.")
            return
        
        try:
            parse(input_file, output_file)
            messagebox.showinfo("Success", f"{input_file} converted successfully into {output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFtoDOCXApp(root)
    root.mainloop()
