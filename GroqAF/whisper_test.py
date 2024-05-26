import os
from groq import Groq
from dotenv import load_dotenv  

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
filename = os.path.dirname(__file__) + "\Audio\Charlie Puth - Attention [Official Video].mp3"

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="whisper-large-v3",
    )
    print(transcription.text)