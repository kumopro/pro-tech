import json
from watson_developer_cloud import TextToSpeechV1

def text2speech(mode="ja"):
    USER_NAME= '4a3d1e76-9132-4f83-b131-122da190f921'
    PASSWORD = 'QmHSjNTK52jt'
    TEXT = '犬'

    text_to_speech = TextToSpeechV1(
        username=USER_NAME,
        password=PASSWORD
        )

    with open('speech_result.mp3', 'wb') as audio_file:
        if mode=="ja":
            audio_file.write(
                text_to_speech.synthesize(
                    TEXT,
                    'audio/mp3',
                    'ja-JP_EmiVoice'
                    ).get_result().content)
        else:
            audio_file.write(
                text_to_speech.synthesize(
                    TEXT,
                    'audio/wav',
                    'en-US_AllisonVoice'
                    ).get_result().content)


text2speech()
