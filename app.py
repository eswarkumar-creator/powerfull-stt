import streamlit as st
from audiorecorder import audiorecorder
from openai import OpenAI

st.title("🎙️ లైవ్ స్పీచ్ టు టెక్స్ట్")

# మీ API Keyతో కలిపిన క్లయింట్ సెటప్
client = OpenAI(api_key="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")

# ఆడియో రికార్డర్
audio = audiorecorder("రికార్డింగ్ మొదలుపెట్టండి", "రికార్డింగ్ ఆపండి")

if len(audio) > 0:
    # ఆడియోను ప్రాసెస్ చేయడం
    audio.export("audio.mp3", format="mp3")
    audio_file = open("audio.mp3", "rb")
    
    with st.spinner('AI మీ మాటలను అర్థం చేసుకుంటోంది...'):
        try:
            transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
            st.subheader("మీరు అన్న మాటలు:")
            st.write(transcript.text)
        except Exception as e:
            st.error(f"Error: {e}")
            
