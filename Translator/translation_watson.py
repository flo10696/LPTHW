
import re
import json
import random
from watson_developer_cloud import LanguageTranslatorV2

class Translator():

    def __init__(self):

        self.language_translator = LanguageTranslatorV2(
            username='c868ee1b-87a7-4380-b1ae-ccb31e284a4c',
            password='4HeTKbs7lpZD')


        self.languages  = {  "en" : ["en-ar", "en-arz", "en-de", "en-es", "en-fr", "en-it", "en-ja", "en-ko", "en-pt"],
                        "ar" : ["ar-en"],
                        "arz" : ["arz-en"],
                        "es" : ["es-en", "es-fr"],
                        "fr" : ["fr-en", "fr-es"],
                        "it" : ["it-en"],
                        "ja" : ["ja-en"],
                        "ko" : ["ko-en"],
                        "pt" : ["pt-en"],
                        "de" : ["de-en"]}

    def translateInput(self, numberOfIterations, textInput):
        
        languageDetection = self.language_translator.identify(textInput)
        startLanguage = languageDetection[u'languages'][0][u'language']
        self.lastTargetLanguage = startLanguage

        for x in range(0, numberOfIterations):

            try:
                direction = self.languages[self.lastTargetLanguage][random.randint(0,len(self.languages[self.lastTargetLanguage])-1)]
            except KeyError:
                return "unable to detect language!"

            m = re.match("(.*)(\-)(.*)", direction)
            self.lastTargetLanguage = m.group(3)
            textInput = self.language_translator.translate(textInput, model_id= direction)

        if self.lastTargetLanguage != 'en':
            textInput = self.language_translator.translate(textInput, source = self.lastTargetLanguage, target='en')

        if startLanguage != 'en':
            textInput = json.dumps(self.language_translator.translate(textInput, source = 'en', target=startLanguage), indent = 2)

        return textInput
