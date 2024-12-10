import os
from gtts import gTTS

def text_to_speech(text, target_language):
    # Define the audio directory
    audio_dir = os.path.join("static", "audio")
    
    # Ensure the directory exists
    os.makedirs(audio_dir, exist_ok=True)

    # Create the audio file path
    audio_file_path = os.path.join(audio_dir, f"{target_language}_output.mp3")

    # Generate and save the audio file
    tts = gTTS(text=text, lang=target_language)
    tts.save(audio_file_path)

    return audio_file_path
