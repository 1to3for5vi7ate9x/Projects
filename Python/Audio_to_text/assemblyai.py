# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "d97fc84da7fc4bc08b9c3dba43bceba3"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("weight.wav")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)