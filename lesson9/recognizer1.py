from watson_developer_cloud import VisualRecognitionV3

def recognize():
    version = '2016-05-20'
    api_key = ''
    filename = ''

    recognizer = VisualRecognitionV3(version=version, iam_apikey=api_key)
    with open (filename, 'rb') as image:
        results = recognizer.classify(image)
    print(results)

recognize()
