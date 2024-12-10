
# LinguaSpeak: NLP Speech Translator 🌍🔊

Welcome to **LinguaSpeak: NLP Speech Translator**! In today's globalized world, effective communication across different languages is essential. This project provides a seamless solution for real-time speech translation and text-to-speech conversion, making language barriers a thing of the past.

![Project Screenshot](static/images/LinguaSpeak_Screenshot.png) <!-- Replace with the actual path or link to your screenshot -->

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Speech to Text Translation** 🎤➡️📝: Translate spoken words into text in real time.
- **Text to Speech Conversion** 📝➡️🔊: Convert written text into natural-sounding speech in multiple languages.
- **Manual Text Input** 🖊️: Double-click the editor to enter text manually.
- **Copy Text Functionality** 📋: Easily copy the translated text with a single click.
- **User-Friendly Interface** 🖥️: Built with [Chakra UI](https://chakra-ui.com/), providing a clean and intuitive user experience.

## Technologies Used

### Frontend
- **Flask**: A lightweight web framework for building the application (serving frontend).
- **React**: Frontend framework (used in conjunction with Chakra UI).
- **Chakra UI**: A modular and accessible component library for React.
- **HTML/CSS/JavaScript**: Core web technologies for frontend development.

### Backend
- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Google Translator**: Library for translating text.
- **gTTS (Google Text-to-Speech)**: A library for converting text to speech using Google APIs.

## Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   └── js
│   └── templates
│       └── index.html
├── models
│   ├── speech_to_text.py
│   ├── text_translation.py
│   └── text_to_speech.py
├── requirements.txt
├── app.py
└── README.md
```

## Installation

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine.
- **Pip**: Package installer for Python.

### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/Dinakarnayak/LinguaSpeak-NLP-Speech-Translator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LinguaSpeak-NLP-Speech-Translator
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Access the application at:
   - Frontend: [http://localhost:5000](http://localhost:5000)

## Usage
- **Speak to Translate**: Click the microphone icon to start speaking. The spoken words will be translated into text.
- **Text to Speech**: Click the speaker icon to convert text to speech in the selected language.
- **Manual Text Input**: Double-click the editor to enter text manually.
- **Copy Text**: Use the copy button to copy translated text.

## Configuration

### Environment Variables
You can add environment variables for any configuration settings needed.

### CORS Configuration
Make sure to configure CORS settings in `app.py` if required. You can add this to handle CORS in FastAPI:
```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (e.g., `git checkout -b feature-branch`).
3. Commit your changes (e.g., `git commit -m 'Add some feature'`).
4. Push to the branch (e.g., `git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
Developed by Dinakar Nayak N. For inquiries, please contact me via [dinakarnayak4248@gmail.com](mailto:dinakarnayak4248@gmail.com).

[LinkedIn: Dinakar Nayak N](https://www.linkedin.com/in/dinakar-nayak-n-125762232/)

Thank you for using **LinguaSpeak: NLP Speech Translator**! We hope you find it helpful and easy to use.😊
