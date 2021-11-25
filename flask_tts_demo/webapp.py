from flask import Flask, render_template, send_from_directory, request
import gtts
import uuid

tmpDir = 'voice/'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tts/tts.html')     # main ui

@app.route('/voice/<path:filename>')
def access_file(filename):  # send generated mp3 file to browser
    return send_from_directory(directory=tmpDir, path=filename)

@app.route('/voice', methods=['POST'])  # send text to server
def voice():
    input = request.values.get('input')
    text = input

    if input:
        tts = gtts.gTTS(text, lang='en-US')         # generate mp3 files

        tmpFilename = str(uuid.uuid4()) + '.mp3'    # create random filename
        fullname = tmpDir + tmpFilename
        tts.save(fullname)                          # save it to voice directory
        return fullname                             # return the filename
    else:
        return "ERR"

if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True, port=5000)