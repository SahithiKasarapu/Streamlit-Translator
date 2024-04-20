from transformers import pipeline 
import os 

def doTranslate(inputText):
    os.environ["api_key"] = ("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")
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    result = translator(inputText, max_length=40)
    return result

