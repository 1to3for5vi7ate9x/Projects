
import speech_recognition as sr
from transformers import GPT2Tokenizer, GPT2LMHeadModel

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")



#from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

user_input = text

inputs = tokenizer(user_input, return_tensors="pt")
outputs = model(**inputs)

# Choose the appropriate logits (e.g., the first set)
logits = outputs.logits[0]

predicted_text = tokenizer.decode(logits, skip_special_tokens=True)
print(f"Model output: {predicted_text}")

