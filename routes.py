import cv2
import pytesseract



app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api/get_text",methods=["GET","POST"])
def handle_image():
	f = dict(request.files)["image"]
	contents = f[0].read()
	nparr = np.fromstring(contents, np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	ret = pytesseract.image_to_string(img)
	return {"text":ret}


if __name__=="__main__":
	app.run()
