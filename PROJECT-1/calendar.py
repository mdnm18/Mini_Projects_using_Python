import calendar
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def display_calendar(year, month):
    cal = calendar.TextCalendar().formatmonth(year, month)
    text.delete("1.0", tk.END)
    text.insert(tk.END, cal)

def save_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    cal = calendar.TextCalendar().formatmonth(year, month)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(cal)
        messagebox.showinfo("Success", f"Calendar saved to {file_path}")

def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        if 1 <= month <= 12:
            display_calendar(year, month)
        else:
            messagebox.showerror("Error", "Please enter a valid month (1-12).")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for year and month.")

app = tk.Tk()
app.title("Digital Calendar")

tk.Label(app, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(app)
year_entry.grid(row=0, column=1)

tk.Label(app, text="Month:").grid(row=1, column=0)
month_entry = tk.Entry(app)
month_entry.grid(row=1, column=1)

tk.Button(app, text="Show Calendar", command=show_calendar).grid(row=2, column=0, columnspan=2)
tk.Button(app, text="Save Calendar", command=save_calendar).grid(row=3, column=0, columnspan=2)

text = tk.Text(app, height=10, width=30)
text.grid(row=4, column=0, columnspan=2)

app.mainloop()
