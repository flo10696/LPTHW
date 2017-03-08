
import json
import random
from watson_developer_cloud import LanguageTranslatorV2

language_translator = LanguageTranslatorV2(
    username='c868ee1b-87a7-4380-b1ae-ccb31e284a4c',
    password='4HeTKbs7lpZD')




languages  = {  "en" : ["en-ar", "en-arz", "en-de", "en-es", "en-fr", "en-it", "en-ja", "en-ko", "en-pt"],
                "ar" : ["ar-en"],
                "arz" : ["arz-en"],
                "es" : ["es-en", "es-fr"],
                "fr" : ["fr-en", "fr-es"],
                "it" : ["it-en"],
                "ja" : ["ja-en"],
                "ko" : ["ko-en"],
                "pt" : ["pt-en"],
                "de" : ["de-en"]}

def translateInput(numberOfIterations, textInput = "What time is it?"):
    languageDetection = language_translator.identify(textInput)
    startLanguage = languageDetection[u'languages'][0][u'language']

    for x in range(0, numberOfIterations):
        languageDetection = language_translator.identify(textInput)
        currentLanguage = languageDetection[u'languages'][0][u'language']

        direction = languages[currentLanguage][random.randint(0,len(languages[currentLanguage])-1)]
        textInput = language_translator.translate(textInput, model_id= direction)

    languageDetection = language_translator.identify(textInput)
    currentLanguage = languageDetection[u'languages'][0][u'language']

    if currentLanguage != 'en':
        textInput = language_translator.translate(textInput, source = currentLanguage, target='en')

    if startLanguage != 'en':
        textInput = json.dumps(language_translator.translate(textInput, source = 'en', target=startLanguage), indent = 2)

    return textInput
print(translateInput(4, "What time is it?"))
