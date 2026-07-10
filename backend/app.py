import logging
from urllib.parse import parse_qs, urlparse

from flask import Flask, jsonify, request
from transformers import pipeline
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
)

# ----------------------------
# Configuration
# ----------------------------

MODEL_NAME = "facebook/bart-large-cnn"
CHUNK_SIZE = 800

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load model only once
logger.info("Loading summarization model...")
summarizer = pipeline(
    "summarization",
    model=MODEL_NAME
)
logger.info("Model loaded successfully.")


# ----------------------------
# Routes
# ----------------------------

@app.get("/summary")
def summarize_video():

    video_id = request.args.get("videoId")

    if not video_id:
        return jsonify({"error": "Missing videoId"}), 400

    logger.info(f"Video ID: {video_id}")

    transcript = get_transcript(video_id)

    summary = generate_summary(transcript)

    return jsonify({
        "summary": summary
    })


# ----------------------------
# Helper Functions
# ----------------------------



def get_transcript(video_id: str) -> str:
    """
    Fetch transcript using youtube-transcript-api 1.2.4
    """

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    return " ".join(
        snippet.text
        for snippet in transcript.snippets
    )


def generate_summary(transcript: str) -> str:
    """
    Split long transcripts into chunks and summarize each chunk.
    """

    chunks = [
        transcript[i:i + CHUNK_SIZE]
        for i in range(0, len(transcript), CHUNK_SIZE)
    ]

    summaries = []

    for chunk in chunks:

        result = summarizer(
            chunk,
            max_length=130,
            min_length=30,
            do_sample=False,
        )

        summaries.append(result[0]["summary_text"])

    return " ".join(summaries)


# ----------------------------
# Entry Point
# ----------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
