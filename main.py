from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = [] 
        if rec_id is not None:
            for key, value in request.files.items():
                print(key, value)
                # upload the file
                file = request.files[key]
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
                    if not os.path.exists(upload_path):
                        os.mkdir(upload_path)
                    file.save(os.path.join(upload_path, filename))
                    input_files.append(file.filename)
                    #capture the description and save it to a file
                    with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"),"w")as f:
                        f.write(desc or "")
            for fl in input_files:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
                    f.write(f"file '{fl}'\nduration 1\n")
        else:
            print("rec_id is None, file not saved.")
            
    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html",reels=reels)


app.run(debug=True)
