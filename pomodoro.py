import tkinter as tk
import threading
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        sekf.hours = 1
        self.minutes = 25
        self.seconds = 0
        self.timer_text = tk.StringVar()
        self.timer_text.set(f"{self.minutes:02d}:{self.seconds:02d}")
        self.timer_label = tk.Label(master, textvariable=self.timer_text, font=("Helvetica", 48))
        self.timer_label.pack(padx=50, pady=50)
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.pause_button = tk.Button(master, text="Pause", command=self.toggle_pause_button)
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.status = "stopped"
        
    def start_timer(self):
        if self.status == "stopped":
            self.status = "running"
            t = threading.Thread(target=self._run_timer)
            t.start()
        elif self.status == "paused":
            self.status = "running"
            
    def _run_timer(self):
        while self.minutes >= 0 and self.seconds >= 0:
            if self.status == "paused":
                time.sleep(0.1)
            else:
                self.update_timer()
                time.sleep(1)
                self.seconds -= 1
                if self.seconds < 0:
                    self.seconds = 59
                    self.minutes -= 1
        
        self.timer_text.set("00:00")
        self.status = "stopped"
        
    def update_timer(self):
        self.timer_text.set(f"{self.minutes:02d}:{self.seconds:02d}")
        self.master.update_idletasks()
        
    def toggle_pause_button(self):
        if self.status == "running":
            self.status = "paused"
            self.pause_button.config(text="Resume")
        else:
            self.status = "running"
            self.pause_button.config(text="Pause")
        
    def reset_timer(self):
        if self.status != "stopped":
            self.status = "stopped"
            self.minutes = 25
            self.seconds = 0
            self.timer_text.set(f"{self.minutes:02d}:{self.seconds:02d}")
            self.thread_stop = True
        else:
            self.minutes = 25
            self.seconds = 0
            self.timer_text.set(f"{self.minutes:02d}:{self.seconds:02d}")

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
