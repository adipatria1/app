from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Use "en" for English (ISO 639-1 code)
    translated_text = english_to_french(textToTranslate, source_language='en')
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Use "fr" for French (ISO 639-1 code)
    translated_text = french_to_english(textToTranslate, source_language='fr')
    return translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
