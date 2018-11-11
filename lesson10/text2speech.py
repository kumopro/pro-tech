import json
from watson_developer_cloud import TextToSpeechV1

def text2speech(text):
    username = '4a3d1e76-9132-4f83-b131-122da190f921'
    password = 'QmHSjNTK52jt'

    text_to_speech = TextToSpeechV1(
        username=username,
        password=password
        )
    r = text_to_speech.synthesize(
        text,
        'audio/mp3',
        'ja-JP_EmiVoice'
        ).get_result().content

    with open('speech_result.mp3', 'wb') as audio_file:
        audio_file.write(r)

text2speech('犬')
