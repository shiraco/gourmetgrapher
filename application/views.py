# coding:utf-8
import os
from flask import request, render_template
from werkzeug import secure_filename
from alchemyapi.alchemyapi import AlchemyAPI

from application import app

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
alchemyapi = AlchemyAPI()


def __allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


def __image_tagging(data):
    result = alchemyapi.imageTagging("image", data)
    return result


@app.route("/", methods=["GET", "POST"])
def upload_file():

    # file upload
    if request.method == "POST":
        file = request.files["file"]
        if file and __allowed_file(file.filename):

            # ファイル名が安全かチェック
            filename = secure_filename(file.filename)

            # ファイルを保存
            file.save(os.path.join(app.config["UPLOAD_DIR"], filename))
            result = __image_tagging(os.path.join(app.config["UPLOAD_DIR"], filename))
            if result["status"] == 'OK':
                image_keywords = result["imageKeywords"]
                return render_template("index.html", name=filename, image_keywords=image_keywords)

    return render_template("index.html")


@app.route("/uploaded_file")
def uploaded_file():
    return "success upload {0}! {1}!".format(request.args["filename"], request.args["tag"])
