from flask import Blueprint, render_template, request, jsonify
from models.text_translation import translate_text
from models.text_to_speech import text_to_speech

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def home():
    return render_template('index.html')

@app_routes.route('/api/translate', methods=['POST'])
def api_translate():
    data = request.json
    text = data.get('text')
    source_language = data.get('source_language')
    target_language = data.get('target_language')
    
    translated_text = translate_text(text, target_language)
    audio_file_path = text_to_speech(translated_text, target_language)
    
    return jsonify({
        'translated_text': translated_text,
        'audio_file_path': audio_file_path
    })
