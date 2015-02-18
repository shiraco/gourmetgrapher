# coding:utf-8
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename

# UPLOAD_FOLDER = "/var/www/uploads/"
UPLOAD_FOLDER = "/Users/shiraishi/Desktop"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def __allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and __allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("uploaded_file", filename=filename))
    return render_template("index.html")


@app.route("/uploaded_file")
def uploaded_file():
    return "success upload %s!".format(request.args["filename"])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
