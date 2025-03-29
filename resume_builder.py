import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

# Function to generate a PDF resume
def generate_resume():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    education = text_education.get("1.0", tk.END).strip()
    skills = text_skills.get("1.0", tk.END).strip()
    experience = text_experience.get("1.0", tk.END).strip()

    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "Please fill all required fields!")
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "RESUME", ln=True, align="C")
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"Name: {name}", ln=True, align="L")
    pdf.cell(200, 10, f"Email: {email}", ln=True, align="L")
    pdf.cell(200, 10, f"Phone: {phone}", ln=True, align="L")
    pdf.cell(200, 10, f"Address: {address}", ln=True, align="L")
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Education:", ln=True, align="L")
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, education)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Skills:", ln=True, align="L")
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, skills)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Work Experience:", ln=True, align="L")
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, experience)

    pdf_filename = f"{name.replace(' ', '_')}_Resume.pdf"
    pdf.output(pdf_filename)
    messagebox.showinfo("Success", f"Resume saved as {pdf_filename}")

# GUI setup
root = tk.Tk()
root.title("Resume Builder")
root.geometry("500x600")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=50)
entry_phone.pack()

tk.Label(root, text="Address:").pack()
entry_address = tk.Entry(root, width=50)
entry_address.pack()

tk.Label(root, text="Education:").pack()
text_education = tk.Text(root, height=5, width=50)
text_education.pack()

tk.Label(root, text="Skills:").pack()
text_skills = tk.Text(root, height=3, width=50)
text_skills.pack()

tk.Label(root, text="Work Experience:").pack()
text_experience = tk.Text(root, height=5, width=50)
text_experience.pack()

tk.Button(root, text="Generate Resume", command=generate_resume).pack(pady=10)

root.mainloop()
