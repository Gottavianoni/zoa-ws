from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import json,os,subprocess,re

UPLOAD_FOLDER = 'uploads/'
TIKA_EXE = 'external/'
TIKA_INPT = 'uploads/temps.pdf'
FULL = os.getcwd()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TIKA_EXE'] = TIKA_EXE
app.config["TIKA_INPT"] = TIKA_INPT
app.config["FULL"] = FULL

@app.route('/')
def hello():
    return "HI on ZOA WS"

@app.route('/pdf-parser', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        cpt = str(len(os.listdir(app.config['UPLOAD_FOLDER'])) +1 )
        file = request.files['file']       
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "file" + cpt + ".pdf" ))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], "file" + cpt + ".pdf") 
        json_done = subprocess.check_output("java -jar " + "/".join(app.config["FULL"].split("\\")) + "/" + "/".join(app.config["TIKA_EXE"].split("\\")) + "tika-app.jar -j  " + "/".join(app.config["FULL"].split("\\")) + "/" + "/".join(file_path.split("\\"))  , shell=True).decode("windows-1252")
        return render_template("pdf-parser.html", Done = json_done)
    return render_template("pdf-parser.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')