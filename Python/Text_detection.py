import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from gtts import gTTS
import os

# Load the image
image = Image.open('image1.png')

# Convert the image to grayscale
image = image.convert('L')

# Apply image enhancement
enhancer = ImageEnhance.Contrast(image)
enhanced_image = enhancer.enhance(2)  # Adjust the enhancement factor as needed

# Apply image filtering
filtered_image = enhanced_image.filter(ImageFilter.SHARPEN)

# Apply OCR and extract text
extract_text = pytesseract.image_to_string(filtered_image)

# Creating text to speech object
tts = gTTS(text=extract_text, lang='en')


# Save the audio file
tts.save('output.mp3')

# Play the audio file
os.system('afplay output.mp3')

# Process the extracted text
print(extract_text)
