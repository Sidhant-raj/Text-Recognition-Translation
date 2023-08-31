from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import Ocr, uuid

app = FastAPI()
IMAGEDIR = "images/"


class TranslatingItems(BaseModel):
    TargetLanguage: str
    ImageName: str


@app.post('/UploadImages/')
async def upload_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.png"
    contents = await file.read()

    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    return {"filename": file.filename}


@app.post('/')
async def Translating_endpoint(item: TranslatingItems):
    translated_texts, sentence = Ocr.StarterFunction(item.TargetLanguage, item.ImageName)
    return {
        "Original text": str(sentence),
        "Translated text": str(translated_texts)
    }

