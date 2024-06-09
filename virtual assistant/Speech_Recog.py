from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS  # google text to speech api
import os  # to save the audio file
import pyttsx3  # conversion of text to speech
from langdetect import detect  # to know what language was used
import pycountry
import subprocess
import pyautogui
import time
import openai

all_languages = (
    'afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
    'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 'bg', 'catalan', 'ca',
    'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn', 'chinese (traditional)', 'zh-tw', 'corsican', 'co',
    'croatian', 'hr', 'czech', 'cs', 'danish', 'da', 'dutch', 'nl', 'english', 'en', 'esperanto', 'eo',
    'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
    'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati', 'gu', 'haitian creole', 'ht', 'hausa', 'ha',
    'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong', 'hmn', 'hungarian', 'hu', 'icelandic', 'is',
    'igbo', 'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it', 'japanese', 'ja', 'javanese', 'jw',
    'kannada', 'kn', 'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)', 'ku', 'kyrgyz', 'ky',
    'lao', 'lo', 'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish', 'lb', 'macedonian', 'mk',
    'malagasy', 'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori', 'mi', 'marathi', 'mr',
    'mongolian', 'mn', 'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 'pashto', 'ps',
    'persian', 'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa', 'romanian', 'ro', 'russian', 'ru',
    'samoan', 'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho', 'st', 'shona', 'sn', 'sindhi', 'sd',
    'sinhala', 'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so', 'spanish', 'es', 'sundanese', 'su',
    'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
    'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek', 'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
    'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu'
)

language_mapping = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
    'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
    'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
    'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
    'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
    'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
    'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
    'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
    'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
    'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa',
    'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
    'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
    'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
    'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
    'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
}

openai.api_key = "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"

# Load the English language model for speech recognition
recognizer = sr.Recognizer()

# Initialize the speech synthesizer
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to capture voice command
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...\n")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Could not understand. Please try again.")
        return None


def transcribe_audio(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Function to send to chat-masigpt
def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

# Function to translate text
def translate_text(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    translated_text = translation.text
    # return translation.text
    target_language = language_mapping[dest_lang]
    ttss = gTTS(text=translated_text, lang=target_language, slow=False)  # Change variable name to tts
    ttss.save("translated_text.mp3")
    audio_files = 'translated_text.mp3'
    playsound(audio_files)
    os.remove(audio_files)  # Remove the audio file after playing

# Function to open Chrome in incognito mode and search query
def open_chrome_incognito_and_search(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    subprocess.Popen(f"start chrome --incognito {url}", shell=True)
    time.sleep(3)  # Wait for Chrome to open
    # Click on the search bar and type the query using pyautogui
    pyautogui.click(x=100, y=100)  # Adjust coordinates as needed
    pyautogui.write(query)
    pyautogui.press('enter')

# Function to read notes
def read_notes():
    with open("output.txt", "r", encoding="utf-8") as f:
        notes = f.read()
        playsound('hereareyournotes.mp3')
        tts = gTTS(text=notes, lang='en', slow=False)
        tts.save("english_notes.mp3")
        original_audio_file = 'english_notes.mp3'
        playsound(original_audio_file)
        os.remove(original_audio_file)  # Remove the audio file after playing

# Function to translate notes
def translate_notes(target_language):
    translator = Translator()
    with open("output.txt", "r", encoding="utf-8") as f:
        notes = f.read()
    translated_notes = translator.translate(notes, dest=target_language).text
    # Open the translatedoutput.txt file in write mode to clear its content
    with open("translatedoutput.txt", "w", encoding="utf-8") as translated_file:
        translated_file.write("")  # Clear the contents of the file
        # Write the new translated text to the file
        translated_file.write(translated_notes)

# Function to read translated notes
def read_translated_notes(target_language):
    try:
        target_language_code = language_mapping[target_language.lower()]
    except KeyError:
        print("Language not found.")
        return
    with open("translatedoutput.txt", "r", encoding="utf-8") as f:
        translated_notes = f.read()
        playsound('translatedversion.mp3')
        tts = gTTS(text=translated_notes, lang=target_language_code, slow=False)  # Change variable name to tts
        tts.save("translated_notes.mp3")
        audio_file = 'translated_notes.mp3'
        playsound(audio_file)
        os.remove(audio_file)  # Remove the audio file after playing

# Function to delete notes
def delete_current_note():
    # Open the output.txt file in write mode to clear its content
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("")  # Clear the contents of the file
        playsound('deletenote.mp3')

print("Welcome to the Voice Assistant!")
playsound('welcometovoiceassitant.mp3')

while True:
    print("Please choose an action:")
    print("1. Talk to Jarvis ")
    print("2. Open Browser")
    print("3. Translate Text")
    print("4. Take Note")
    print("5. Stop Program")

    choice = take_command()

    if choice == "talk to jarvis":
        print("You selected: Talk to Jarvis AI")
        speak("Please talk to Jarvis AI.")

        messages = [{"role": "user", "content": "Please act like Jarvis from Iron man."}]
        while True:
            text = take_command()

            if text == "stop":
                break

            messages.append({"role": "user", "content": text})
            response = send_to_chatGPT(messages)
            speak(response)

            print(response)

    elif choice == "open browser":
        print("You selected: Open Browser")
        speak("What do you want to search?")
        query = take_command()
        if query:
            open_chrome_incognito_and_search(query)

    elif choice == "translate text":
        print("You selected: Translate Text")
        speak("Please speak the text you want to translate.")
        text = take_command()
        if text:
            speak("In which language do you want to translate?")
            dest_lang = take_command()
            if dest_lang:
                dest_lang = dest_lang.lower()
                if dest_lang in all_languages:
                    translation = translate_text(text, dest_lang)
                    # speak(f"The translated text is: {translation}")
                else:
                    speak("Language not supported.")

    elif choice == "take note":
        print("You selected: Take Note")
        takenote = 'noteoption.mp3'
        playsound(takenote)
        os.remove(takenote)

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        notes_in_progress = False
        target_language = 'en'  # Default language for translated notes
        while True:
            text = transcribe_audio(recognizer, microphone)
            if "begin note" in text.lower():
                notes_in_progress = True
                print("Note-taking started.")
            elif "stop note" in text.lower():
                notes_in_progress = False
                print("Note-taking ended.")
            elif "end program" in text.lower():
                playsound('zetadadah.mp3')
                print("Program ended.")
                break
            elif "read the note" in text.lower():
                read_notes()
            elif "translate to" in text.lower():
                target_language = text.split("translate to")[-1].strip()
                translate_notes(target_language)
                print("Translation completed.")
            elif "read translated notes" in text.lower():
                read_translated_notes(target_language)  # Pass target_language as argument
            elif "delete current note" in text.lower():
                delete_current_note()  # Call the delete_current_note function
                print("Current note deleted.")
            elif notes_in_progress:
                with open("output.txt", "a", encoding="utf-8") as f:
                    f.write(text + "\n")

    elif choice == "stop program":
        print("Program will be stopped")
        playsound('zetadadah.mp3')
        break

    else:
        print("Invalid choice. Please try again.")
        speak("Invalid choice. Please try again.")
