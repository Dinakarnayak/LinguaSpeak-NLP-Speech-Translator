let audioFilePath = '';

async function translateText() {
    const sourceLanguage = document.getElementById('source-language').value;
    const targetLanguage = document.getElementById('target-language').value;
    const text = document.getElementById('input-text').value;

    const response = await fetch('/api/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, source_language: sourceLanguage, target_language: targetLanguage })
    });

    const data = await response.json();
    document.getElementById('translated-text').value = data.translated_text;
    audioFilePath = data.audio_file_path;
}

function playTextToSpeech() {
    if (audioFilePath) {
        const audio = new Audio(audioFilePath);
        audio.play();
    }
}
