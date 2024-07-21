from pydub import AudioSegment
import speech_recognition as sr

# Paths to your input MP3 file and output WAV file
input_mp3_path = "Weight.mp3"
output_wav_path = "Weight.wav"
output_text_path = "transcription.txt"

# Step 1: Convert MP3 to WAV
def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    print(f"Converted {mp3_path} to {wav_path}")

# Step 2: Transcribe the WAV file using pocketsphinx
def transcribe_audio(wav_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_sphinx(audio_data)
            print("Transcription: ")
            print(text)
            return text
        except sr.UnknownValueError:
            print("PocketSphinx could not understand the audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from PocketSphinx service; {e}")
            return ""

# Step 3: Save transcription to a text file
def save_transcription(text, text_path):
    with open(text_path, "w") as text_file:
        text_file.write(text)
    print(f"Transcription saved to {text_path}")

# Main function
if __name__ == "__main__":
    convert_mp3_to_wav(input_mp3_path, output_wav_path)
    transcription = transcribe_audio(output_wav_path)
    if transcription:
        save_transcription(transcription, output_text_path)
