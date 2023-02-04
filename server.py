import time
import uuid
import os
from speech_recognition import recognize
from flask import Flask, request, send_file
from flask_cors import CORS
import os
import shutil
cwd = os.getcwd()


app = Flask(__name__)
CORS(app)

folder = './recordings'
os.makedirs(folder, exist_ok=True)


def clear_directory():
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def saveAudioFile(content, file_name):
    file_path = os.path.join(folder, file_name)

    with open(file_path, 'wb') as file:
        file.write(content)

    return file_path


@app.route('/transcript', methods=['POST'])
def get_transcript():
    content = request.files['sample'].read()
    file_name = f'recording-{uuid.uuid1()}.wav'
    file_path = saveAudioFile(content, file_name)
    text = recognize([file_path])

    # os.remove(file_path)
    clear_directory()

    return {'data': text}


@app.route('/')
def get_index():
    return '''<h2>API:</h2>
      <code>
        POST <a href="http://localhost:5000/transcript">http://localhost:5000/transcript</a>
        <br/>    
        FormData <b>{ sample: Blob (binary); }</b> <i>// audio/wav binary blob</i>
      </code>'''


if __name__ == "__main__":
    app.run(debug=True)
