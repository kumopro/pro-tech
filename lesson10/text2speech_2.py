import json
from watson_developer_cloud import TextToSpeechV1

def text2speech(text, filename, mode='ja'):
    username = ''
    password = ''

    text_to_speech = TextToSpeechV1(
        username=username,
        password=password
        )
    if mode=='ja':
        voice_mode = 'ja-JP_EmiVoice'
    else:
        voice_mode = 'en-US_AllisonVoice'

    text_to_speech.synthesize(
        text,
        'audio/mp3',
        voice_mode
        ).get_result().content

    with open(filename, 'wb') as audio_file:
        audio_file.write(r)

text2speech('dog', 'result_en.mp3', mode='en')
text2speech('犬', 'result_ja.mp3', mode='ja')
