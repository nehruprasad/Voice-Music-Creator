
# Voice Music Creator 🎵

A **Streamlit-based Python application** that generates custom music tracks based on textual descriptions.  
Users can describe the music, generate a MIDI track, play it, and download it.

---

## **Features**

1. **Describe Music**  
   - Enter a textual description of the desired music (e.g., "happy piano melody with drums").

2. **System Composes MIDI**  
   - Generates a MIDI track based on the description (currently uses a simple random note mapping algorithm).

3. **Playback Controls**  
   - Play the generated MIDI track directly in the browser.

4. **Download MIDI Track**  
   - Download the generated track for personal use.

---

## **Requirements**

- Python 3.8+  
- Streamlit  
- numpy  
- mido  
- pygame  
- pydub  

Install dependencies:

```bash
pip install streamlit numpy mido pygame pydub
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository-url>
cd voice-music-creator
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows

bash
Copy code
venv\Scripts\activate
Linux / Mac

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the App
Ensure your virtual environment is active.

Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the URL displayed in the terminal (usually http://localhost:8501).

Enter a music description.

Click Generate Music to create a MIDI track.

Play it using the audio player and download it using the button provided.

Sample Input
Description:

csharp
Copy code
Happy piano melody with drums and light bass
Expected Output
Generated MIDI Track

Audio player in the browser to play the track.

Download Option

Downloadable custom_track.mid file for personal use.

