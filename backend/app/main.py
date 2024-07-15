from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import easyocr
import fitz
from PIL import Image
import numpy as np
from TTS.api import TTS
import torch
import logging
app = FastAPI()
# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"

def read_pdf(file_path):
    try:
        reader = easyocr.Reader(['en'])
        text = ""
        pdf_document = fitz.open(file_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            result = reader.readtext(np.array(img))
            page_text = " ".join([res[1] for res in result])
            text += page_text + "\n"
        return text
    except Exception as e:
        logger.error(f"Error in read_pdf: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {str(e)}")
def generate_audio(text):
    try:
        tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(device)
        output_file = "/tmp/output.wav"
        tts.tts_to_file(text=text, file_path=output_file)
        if os.path.exists(output_file):
            logger.info(f"Audio file created at {output_file}")
        else:
            raise Exception("Failed to create audio file.")
        return output_file
    except Exception as e:
        logger.error(f"Error in generate_audio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating audio: {str(e)}")
@app.get('/')
async def root():
    return {"MESSAGE": "WELCOME TO OUR SITE VISITING"}
@app.post("/pdf_to_audio")
async def pdf_to_audio(file: UploadFile = File(...)):
    logger.info(f"Received file: {file.filename}")
    try:
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())

        text = read_pdf(file_location)
        audio_file = generate_audio(text)

        if not os.path.exists(audio_file):
            raise HTTPException(status_code=500, detail="Audio file was not created successfully.")

        return FileResponse(audio_file, media_type='audio/wav', filename="output.wav")
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Unexpected error in pdf_to_audio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")