# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")
# string = '''티티에스의 사실상의 표준이 마이크로소프트 루틴과 네오스피치 포맷의 음성 패키지인지라,
# 보이스웨어의 음성 역시 이에 호환되기 때문에 국내에서는 티티에스는 보이스웨어 같은 식으로 반쯤 동의어처럼 사용되고 있다.
# 실은 다른 티티에스 소프트웨어에서 보이스웨어 사의 음성을 사용하는 것도 얼마든지 가능하다.

# 마찬가지로 보이스웨어라는 것은 우리말 티티에스 상품의 브랜드 이름일 뿐이고,
# 다른 회사가 다른 상품명을 달고 한국어 TTS를 판매하면,
# 그것은 엄연이 보이스웨어가 아닌 'TTS'이다.'''
# engine.save_to_file(string, 'speech2.mp3')
# engine.runAndWait()

from flask import Flask, jsonify, request
from flask_cors import CORS
import pyttsx3
import vlc
from vlcPlayer import VlcPlayer
import threading
import time

engine = pyttsx3.init()

app = Flask(__name__)
CORS(app)


@app.route('/')
def main_page():
    return 'hello world'


@app.route('/voices', methods=['GET'])
def voices():
    r = []
    voices = engine.getProperty('voices')
    for voice in voices:
        v = {}
        v['id'] = voice.id
        v['name'] = voice.name
        v['languages'] = voice.languages
        v['age'] = voice.age
        r.append(v)
    return jsonify({'voices': r})


@app.route('/synth', methods=['GET'])
def synth():
    try:
        name = request.args.get('name') + '.mp3'
        docs = request.args.get('docs')
        print(name, docs)

        engine.save_to_file(docs, name)
        engine.runAndWait()
        return jsonify({'result': 'success', 'name': name})
    except:
        return jsonify({'result': 'fail'})

# def gettime(event, ms):
#     print('play1 - ', event)

def stop(event):
    print('player stop')
    global status
    status = 1

@app.route('/play')
def playWeb():
    play()


def play():
    player = VlcPlayer()
    player.add_callback(vlc.EventType.MediaPlayerStopped, stop)
    player.add_callback_timer()
    player.play('1.mp4')

    status = 0
    while True:
        if status == 1:
            break
        else:
            time.sleep(0.5)

    return "play ok"

if __name__ == '__main__':
    play()

