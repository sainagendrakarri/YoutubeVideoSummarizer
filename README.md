![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
# YouTube Video Summariser

A Chrome extension that generates concise summaries of YouTube videos by extracting video transcripts and processing them with a Transformer-based NLP model. The project consists of a Flask backend API and a Chrome extension frontend.

---

## Features

- Summarizes long YouTube videos in seconds
- Extracts transcripts using the YouTube Transcript API
- Uses Hugging Face Transformers for NLP-based summarization
- Simple Chrome extension interface
- Supports long videos through transcript chunking

---

## Tech Stack

- Python
- Flask
- Hugging Face Transformers
- YouTube Transcript API
- HTML
- JavaScript
- Chrome Extension API

---

## Project Structure

```
youtube-video-summariser/
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── icon.png
│
├── screenshots/
├── README.md
└── .gitignore
```

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r backend/requirements.txt
```

3. Start the Flask server

```bash
python backend/app.py
```

4. Open Chrome

5. Navigate to

```
chrome://extensions
```

6. Enable **Developer Mode**

7. Click **Load unpacked**

8. Select the `extension` folder.

---

## Usage

1. Start the Flask backend.
2. Open any YouTube video.
3. Click the extension icon.
4. Wait for the summary to be generated.

---

## Future Improvements

- Multi-language transcript support
- Adjustable summary length
- Better UI/UX
- Caching for faster summaries
- Support for Gemini/OpenAI summarization

---


