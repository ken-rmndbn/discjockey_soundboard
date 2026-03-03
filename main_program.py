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

