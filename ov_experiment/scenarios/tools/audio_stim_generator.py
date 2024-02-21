import pygame
import numpy as np
import scipy.io.wavfile as wavfile
import os

# Initialize pygame
pygame.mixer.init()

def generate_sound(frequency, duration, sampling_rate=44100):
    # Generate the sound array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    audio_data = np.sin(2 * np.pi * frequency * t)

    # Normalize audio data to 16-bit range
    audio_data_normalized = np.int16(audio_data * 32767)

    return sampling_rate, audio_data_normalized

def save_sound(filename, frequency, duration):
    sampling_rate, audio_data = generate_sound(frequency, duration)
    wavfile.write(filename, sampling_rate, audio_data)

# Example usage
if __name__ == "__main__":
    start = os.path.dirname(__file__)
    fileDir = os.path.abspath(os.path.join(start, "..", "assets"))
    filePath_non_freq = os.path.join(fileDir, "non_freq.wav")
    filePath_freq = os.path.join(fileDir, "freq.wav")
    save_sound(filePath_non_freq, 1500, 2)
    save_sound(filePath_freq, 1000, 2)
