from transformers import pipeline 
import os 

def doTranslate(inputText, target_language):
    os.environ["api_key"] = ("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")
    translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-en-{target_language}")
    result = translator(inputText, max_length=40)
    return result[0]['translation_text']
