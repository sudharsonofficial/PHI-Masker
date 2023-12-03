from flask import Flask, render_template, redirect, jsonify, request
from processor import Processor

app = Flask("__main__")
processor = Processor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST","GET"])
def predict():
    if request.method == "POST":
        text = request.form["res"]

        masked_text = processor.process(text)
        # print(masked_text)

        return jsonify(masked_text)


if __name__ == "__main__":
    app.run(debug=True,port=2000)