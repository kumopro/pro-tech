import json
from watson_developer_cloud import LanguageTranslatorV3

def translate():
    WVR_VERSION = '2018-05-01'
    WVR_API_KEY = 'FcHA3xI6U7H2QaTQ9jiwwkNvWRgmwIK_VgkTeB6HjFSF'
    TEXT = 'dog'


    translator = LanguageTranslatorV3(version=WVR_VERSION, iam_apikey=WVR_API_KEY)

    results = translator.translate(text=TEXT, model_id='en-ja').get_result()
    r = results['translations'][0]['translation']
    print(r)

translate()
