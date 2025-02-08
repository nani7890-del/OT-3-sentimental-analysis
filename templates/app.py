from flask import Flask, render_template,request
app = Flask(_name_)
@app.route("/")
def Home():
    return render_template("index.html")
@app.route("/predict")
def predict():
    return render_templpate("predict.html")

if _name_ == "_main_":
    app.run(host="0.0.0.0",port=5050)