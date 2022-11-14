# -*- coding: utf-8 -*-

import sys
import numpy as np
import librosa

from monophonic import wave_to_midi


def run():
    print("Starting...")
    # sys.argv[1]
    file_in = "C:\\Users\\tkich\\Downloads\\1_22072022032949Connie Hau_侯慧寧_為了假裝可有多盡_Jmix_Mastered_(Vocals).mp3"
    file_out = "melody.txt"  # sys.argv[2]
    audio_data, srate = librosa.load(file_in, sr=None)
    print("Audio file loaded!")
    midi = wave_to_midi(audio_data, srate=srate)
    print("Conversion finished!")
    with open(file_out, 'w', encoding='utf8') as file:
        for line in midi:
            file.write("{:.3f},".format(line[0]) + "{:.3f},".format(line[1]) + str(line[2]) + "," + line[3] + "\n")
    print("Done. Exiting!")


if __name__ == "__main__":
    run()
