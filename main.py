import os

# Install all required modules if not installed
try:
    import PyPDF2
except ImportError:
    os.system('pip install PyPDF2')


try:
    from googletrans import Translator
except ImportError:
        os.system('pip install googletrans==3.1.0a0')


try:
    from gtts import gTTS
except ImportError:
    os.system('pip install gTTS')

# Imports
import PyPDF2
from googletrans import Translator,LANGUAGES
from gtts import gTTS





# USER CUSTOMISATION

#PDF name
pdf_name = input("Enter the PDF name: ")
print("\n")

# Print supported translation languages
print("Supported Languages")
for lang in LANGUAGES:
    print(f'{lang} - {LANGUAGES[lang]}')
print("\n")
# Destination language
trans_lang = input("Choose the desired language to translate from above: ")





# End audio output filename
pdf_to_mp3_name = pdf_name.replace(".pdf","")
audio_name = pdf_to_mp3_name + '.mp3'

# Define Translator
translator = Translator()

# Read the PDF
pdf_open = open(pdf_name, 'rb')
pdf_read = PyPDF2.PdfFileReader(pdf_open)

# Extract PDF text
pdf_pages = pdf_read.numPages
pdf_text = ''
for pg_no in range(0, pdf_pages):
    pdf_page = pdf_read.getPage(pg_no)
    pdf_text = pdf_text + pdf_page.extractText()

# Translate the extracted text
translated = translator.translate(pdf_text, dest=trans_lang)
translated = translated.text

# Convert the translated text to speech as an object
myobj = gTTS(text=translated, lang=trans_lang, slow=False)

# Save it
myobj.save(audio_name)

# Play it
os.system(audio_name)