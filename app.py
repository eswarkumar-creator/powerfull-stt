import streamlit as st
from audiorecorder import audiorecorder
from openai import OpenAI

st.title("🎙️ లైవ్ స్పీచ్ టు టెక్స్ట్")

# మీ OpenAI API కీని ఇక్కడ ఇవ్వండి
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# ఆడియో రికార్డర్
audio = audiorecorder("రికార్డింగ్ మొదలుపెట్టండి", "రికార్డింగ్ ఆపండి")

if len(audio) > 0:
    audio.export("audio.mp3", format="mp3")
    audio_file = open("audio.mp3", "rb")
    
    with st.spinner('ట్రాన్స్‌క్రిప్షన్ జరుగుతోంది...'):
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
        st.subheader("మీరు అన్న మాటలు:")
        st.write(transcript.text)
        
