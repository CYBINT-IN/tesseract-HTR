import cv2
import pytesseract
import numpy as np
from os import path, walk
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api/get_text",methods=["GET","POST"])
def handle_image():
	f = dict(request.files)["image"]
	contents = f.read()
	nparr = np.fromstring(contents, np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	ret = pytesseract.image_to_string(img)
	return render_template("output.html", text=ret)


extra_dirs = ['directory/to/watch',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)


if __name__=="__main__":
	app.run(host='0.0.0.0', extra_files=extra_files)
