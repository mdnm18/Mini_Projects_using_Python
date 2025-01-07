import tkinter as tk
from tkinter import ttk
import time
import threading

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Stopwatch")
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.running = False
        self.laps = []

        self.time_label = ttk.Label(self.root, text="00 : 00 : 00", font=("Helvetica", 48))
        self.time_label.pack()

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0)

        self.pause_button = ttk.Button(self.button_frame, text="Pause", command=self.pause)
        self.pause_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2)

        self.lap_button = ttk.Button(self.button_frame, text="Lap", command=self.lap)
        self.lap_button.grid(row=1, column=0, columnspan=3)

        self.lap_listbox = tk.Listbox(self.root)
        self.lap_listbox.pack()

        self.update_clock()

    def update_clock(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
            if self.hours == 24:
                self.hours, self.minutes, self.seconds = 0, 0, 0

            self.time_label.config(text=f"{self.hours:02d} : {self.minutes:02d} : {self.seconds:02d}")
        self.root.after(1000, self.update_clock)

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.time_label.config(text="00 : 00 : 00")
        self.laps.clear()
        self.lap_listbox.delete(0, tk.END)

    def lap(self):
        lap_time = f"{self.hours:02d} : {self.minutes:02d} : {self.seconds:02d}"
        self.laps.append(lap_time)
        self.lap_listbox.insert(tk.END, lap_time)

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
