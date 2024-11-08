from gtts import gTTS
import os

SUPPORTED_TTS_LANGUAGES = {
    'en': 'English', 'hi': 'Hindi', 'es': 'Spanish', 'fr': 'French', 'de': 'German',
    'zh': 'Chinese', 'ja': 'Japanese', 'ru': 'Russian', 'pt': 'Portuguese', 'ar': 'Arabic',
    # add more languages supported by gTTS as needed
}

def text_to_speech(text, language):
    # Fallback to English if the target language is not supported by gTTS
    if language not in SUPPORTED_TTS_LANGUAGES:
        language = 'en'
    tts = gTTS(text=text, lang=language)
    audio_file_path = f"static/audio/{text[:10]}_output.mp3"
    tts.save(audio_file_path)
    return audio_file_path
