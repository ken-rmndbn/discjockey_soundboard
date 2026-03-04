import tkinter as tk
from tkinter import messagebox
import pygame

pygame.mixer.init()

window = tk.Tk()
window.title("DJ Soundboard")
window.geometry("500x520")
window.configure(bg="#1e1e1e")

sounds = {"Laugh": "laugh_sound.mp3",
          "Sad": "sad_sound.mp3",
          "Applause": "applause_sound.mp3",
          "Call": "call_sound.mp3",
          "New Year": "newyear_sound.mp3"
         }

def play_sound(name, file):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(volume_slider.get())
        pygame.mixer.music.play(-1)
        status_label.config(text=f"Playing: {name}")
    except:
        messagebox.showerror("Error", f"Cannot play {file}")

def stop_sound():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

def change_volume(value):
    pygame.mixer.music.set_volume(float(value))
    volume_value_label.config(text=f"{int(float(value)*100)}%")

title = tk.Label(window,
                 text = "SOUNDBOARD PAD",
                 font =("Arial", 18, "bold"),
                 bg ="#1e1e1e",
                 fg = "white")
title.pack(pady = 20)

grid_frame = tk.Frame(window, bg = "#1e1e1e")
grid_frame.pack()

sound_list = list(sounds.items())

for i in range (3):
    name, file = sound_list[i]
    btn = tk.Button(grid_frame,
                    text = name,
                    width = 15,
                    height = 5,
                    bg = "#333333",
                    fg = "white",
                    activebackground = "#98FF98",
                    font = ("Arial", 10, "bold"),
                    command = lambda n = name, f = file: play_sound(n, f))
    btn.grid(row = 0, column = i, padx = 10, pady = 10)

for i in range (3, 5):
    name, file = sound_list[i]
    btn = tk.Button(grid_frame,
                    text = name,
                    width = 15,
                    height = 5,
                    bg = "#333333",
                    fg = "white",
                    activebackground = "#98FF98",
                    font = ("Arial", 10, "bold"),
                    command = lambda n = name, f = file: play_sound(n, f))
    btn.grid(row = 1, column = i-3, padx=10, pady=10)

stop_btn = tk. Button(window,
                      text = "STOP",
                      width = 25,
                      bg = "red",
                      fg = "white",
                      activebackground = "black",
                      font = ("Arial", 11, "bold"),
                      command = stop_sound)
stop_btn.pack(pady = 15)

volume_label = tk.Label(window,
                        text = "VOLUME",
                        bg = "#1e1e1e",
                        fg = "white",
                        font = ("Arial", 12, "bold"))
volume_label.pack()

volume_slider = tk.Scale(window,
                         from_ = 0,
                         to = 1,
                         resolution = 0.01,
                         orient = "horizontal",
                         length = 300,
                         bg = "#1e1e1e",
                         fg = "white",
                         highlightthickness = 0,
                         command = change_volume)
volume_slider.set(0.5)
volume_slider.pack()

volume_value_label = tk.Label(window,
                              text = "50%",
                              bg = "#1e1e1e",
                              fg = "white")
volume_value_label.pack()

status_label = tk.Label(window,
                        text = "NO SOUND PLAYING",
                        bg = "#1e1e1e",
                        fg = "white",
                        font = ("Arial", 10, "italic"))
status_label.pack(pady = 10)

window.mainloop()
