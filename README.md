# Steganography API

Hide and reveal secret messages inside images.

## Run with Docker

```bash
docker compose up --build
```

## Run without Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## Usage

Open http://localhost:8000/docs to test the endpoints interactively.

### POST /hide

Upload an image + a message. Returns a PNG with the message hidden inside.

### POST /reveal

Upload an image with a hidden message. Returns the message as JSON.
