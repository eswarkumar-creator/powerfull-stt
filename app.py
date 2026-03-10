import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="POWERFULL STT", page_icon="🎙️")
st.title("🎙️ POWERFULL SPEECH TO TEXT")

# మీ API Key ఇక్కడ సెట్ చేయబడింది
client = OpenAI(api_key="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")

audio_file = st.file_uploader("ఆడియో ఫైల్‌ను అప్‌లోడ్ చేయండి", type=['mp3', 'wav', 'm4a'])

if st.button("టెక్స్ట్‌గా మార్చండి"):
    if audio_file:
        with st.spinner('AI మీ మాటలను అర్థం చేసుకుంటోంది...'):
            try:
                # Whisper AI మోడల్ ఉపయోగించి ఆడియోను టెక్స్ట్ గా మారుస్తున్నాము
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
                st.success("పూర్తయింది!")
                st.subheader("రిజల్ట్:")
                st.write(transcript.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("ముందుగా ఒక ఆడియో ఫైల్‌ని ఎంచుకోండి.")
      
