import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init() # Initialize Pygame mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1920x1045")

        # Create buttons for opening & playing/pausing audio files
        self.open_button = tk.Button(root, text="+", command=self.open_audio)
        self.play_pause_button = tk.Button(root, text="Play/Pause", state=tk.NORMAL, command=self.play_pause_audio)

        self.open_button.pack(padx=10, pady=10, anchor='ne')
        self.play_pause_button.pack(side=tk.BOTTOM, pady=10)

        self.playlist = []

        pygame.mixer.init() # Initialize pygame

        root.protocol("WM_DELETE_WINDOW", self.on_closing) # Register a callback to stop audio when the window is closed

        self.paused = True # Initialize playback state

    def open_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.flac *.mp3 *.wav")])
        if file_path:
            self.audio_file = file_path
            file_name = os.path.basename(file_path)
            song = tk.Button(root, text=file_name)
            song.pack()
            self.playlist.append(file_path)
            pygame.mixer.music.load(self.audio_file)

    def play_pause_audio(self):
        if not pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.play()
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def on_closing(self):
        if pygame.mixer.music.get_busy(): # Check if audio is currently playing
            pygame.mixer.music.stop() # Stop audio playback before closing the application
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

