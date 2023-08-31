import cv2 as cv
import pytesseract
from PIL import Image
from deep_translator import GoogleTranslator


def detect_and_translate(text, targetLang='en'):

    translate = GoogleTranslator(source='auto', target=targetLang)
    return translate.translate(text=text)


def StarterFunction(target_lang: str, fileName):
    Path = "images/" + fileName
    Img = cv.imread(Path, 0)
    _, binary_image = cv.threshold(Img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # cv.imshow("Img", binary_image)
    # cv.waitKey(0)
    input_text = pytesseract.image_to_string(Image.fromarray(binary_image))
    translated_text = detect_and_translate(input_text, target_lang.lower())

    return translated_text, input_text
