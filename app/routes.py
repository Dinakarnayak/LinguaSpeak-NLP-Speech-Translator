from flask import Blueprint, render_template, request, jsonify
from models.text_translation import translate_text
from models.text_to_speech import text_to_speech

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def home():
    return render_template('index.html')

@app_routes.route('/api/translate', methods=['POST'])
def api_translate():
    text = request.json.get('text')
    source_language = request.json.get('source_language')
    target_language = request.json.get('target_language')
    
    # Translate text
    translated_text = translate_text(text, target_language)
    
    # Generate speech for the translated text
    audio_file_path = text_to_speech(translated_text, target_language)
    
    return jsonify({
        'translated_text': translated_text,
        'audio_file_path': audio_file_path
    })
