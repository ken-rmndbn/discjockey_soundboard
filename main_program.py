import tkinter as tk
from tkinter import messagebox
import pygame

pygame.mixer.init()

windows = tk.Tk()
windows.title("DJ Soundboard")
windows.geometry("500x520")
windows.configure(bg="1e1e1e")

sound_list = {"Laugh": "laugh_sound.mp3",
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
        status_label.config(text=f"Looping: {name}")
    except:
        messagebox.showerror("Error", f"Cannot play {file}")

def stop_sound():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

def change_volume(value):
    pygame.mixer.music.set_volume(float(value))
    volume_value_label.config(text=f"{int(float(value)*100)}%")


