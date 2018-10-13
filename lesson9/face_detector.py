from watson_developer_cloud import VisualRecognitionV3
import json

def recognize():
    version = '2018-03-19'
    api_key = 'outJYFDh3fDNNwJcqQIzb09rDNAqZX-5iwJvilfENioc'
    filename = 'obama.jpg'

    recognizer = VisualRecognitionV3(version=version, iam_apikey=api_key)
    with open (filename, 'rb') as image:
        results = recognizer.detect_faces(image).get_result()

    print(json.dumps(results))
    r = results['images'][0]['faces']

    for i in range(1):
        print(r[i])

recognize()