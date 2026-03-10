from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from io import BytesIO
from engine.steganography import hide_msg, reveal_msg
from fastapi import Form
from fastapi.responses import StreamingResponse
app = FastAPI()

@app.post("/hide")
async def hide_message(image: UploadFile = File(...), message: str = Form(...)):
    file_bytes = await image.read()
    input_buffer = BytesIO(file_bytes)
    image_with_message = hide_msg(input_buffer, message)
    output_buffer = BytesIO()
    image_with_message.save(output_buffer, format='PNG')
    output_buffer.seek(0)
    return StreamingResponse(output_buffer, media_type="image/png")

@app.post("/reveal")
async def reveal_message(image: UploadFile = File(...)):
    file_bytes = await image.read()
    input_buffer = BytesIO(file_bytes)
    message = reveal_msg(input_buffer)
    return {"message": message}