import streamlit as st
import mido
from mido import Message, MidiFile, MidiTrack
import numpy as np
import pygame
from tempfile import NamedTemporaryFile
import time

# ----------------- Helper Functions -----------------

NOTE_MAPPING = {
    'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71
}

def generate_midi(description, filename="output.mid", length=32):
    """
    Generate a simple MIDI track based on description (dummy algorithm)
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    tempo = 500000  # microseconds per beat
    track.append(mido.MetaMessage('set_tempo', tempo=tempo))

    # Simple logic: map words to random notes
    words = description.lower().split()
    notes = list(NOTE_MAPPING.values())
    for i in range(length):
        note = np.random.choice(notes)
        track.append(Message('note_on', note=note, velocity=64, time=120))
        track.append(Message('note_off', note=note, velocity=64, time=240))
    
    mid.save(filename)
    return filename

def play_midi(file_path):
    """
    Play MIDI file using pygame
    """
    try:
        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # stereo
        buffer = 1024   # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        st.error(f"Error playing MIDI: {e}")

# ----------------- Streamlit App -----------------

st.set_page_config(page_title="Voice Music Creator", layout="wide")
st.title("🎵 Voice Music Creator")

st.markdown("Describe the music you want, and the system will generate a MIDI track for playback and download.")

# User description input
music_description = st.text_area("Describe the music (e.g., 'happy piano melody with drums')", height=150)

if st.button("Generate Music"):
    if music_description.strip() == "":
        st.warning("Please enter a music description.")
    else:
        st.success("Generating MIDI track...")
        # Generate MIDI
        midi_file_path = generate_midi(music_description)
        st.audio(midi_file_path)
        st.write("✅ MIDI track generated! Use the audio player above to listen.")

        # Provide download option
        with open(midi_file_path, "rb") as f:
            st.download_button(
                label="Download MIDI",
                data=f,
                file_name="custom_track.mid",
                mime="audio/midi"
            )
