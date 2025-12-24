import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init() # Initialize Pygame mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1920x1080")

        # Create buttons for opening, playing, pausing, and resuming audio files
        self.open_button = tk.Button(root, text="+", command=self.open_audio)
        self.play_button = tk.Button(root, text="Play", state=tk.DISABLED, command=self.play_audio)
        self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_audio)
        self.resume_button = tk.Button(root, text="Resume", state=tk.DISABLED, command=self.resume_audio)

        self.open_button.pack(padx=10, pady=10, anchor='ne')
        self.play_button.pack()
        self.pause_button.pack()
        self.resume_button.pack()

        pygame.mixer.init() # Initialize pygame

        root.protocol("WM_DELETE_WINDOW", self.on_closing) # Register a callback to stop audio when the window is closed

        self.paused = False # Initialize playback state

    def open_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.audio_file = file_path
            self.play_button.config(state=tk.NORMAL)
            # Displays the selected file name
            file_name = os.path.basename(file_path)
            label = tk.Label(root, text=file_name)
            label.pack(pady=20)

    def play_audio(self):
        pygame.mixer.music.load(self.audio_file)
        pygame.mixer.music.play()
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

    def pause_audio(self):
        pygame.mixer.music.pause()
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)
        self.paused = True

    def resume_audio(self):
        pygame.mixer.music.unpause()
        self.resume_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.paused = False

    def on_closing(self):
        if pygame.mixer.music.get_busy(): # Check if audio is currently playing
            pygame.mixer.music.stop() # Stop audio playback before closing the application
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

