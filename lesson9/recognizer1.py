from watson_developer_cloud import VisualRecognitionV3
import json

def recognize():
    version = '2018-03-19'
    api_key = 'outJYFDh3fDNNwJcqQIzb09rDNAqZX-5iwJvilfENioc'
    filename = 'dog.jpg'

    recognizer = VisualRecognitionV3(version=version, iam_apikey=api_key)
    with open(filename, 'rb') as image:
        results = recognizer.classify(image).get_result()
    # print(json.dumps(results, indent=2))
    r = results['images'][0]['classifiers'][0]['classes']

    print(r[0]['class'])

recognize()
