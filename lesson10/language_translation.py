import json
from watson_developer_cloud import LanguageTranslatorV3

def translate(text_en):
    version = '2018-05-01'
    api_key = 'FcHA3xI6U7H2QaTQ9jiwwkNvWRgmwIK_VgkTeB6HjFSF'

    translator = LanguageTranslatorV3(version=version, iam_apikey=api_key)

    results = translator.translate(text=text_en, model_id='en-ja').get_result()
    r = results['translations'][0]['translation']
    print(r)

translate('dog')
