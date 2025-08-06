from flask import Flask, request, render_template
from src.predict import predict_cell

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        image_file = request.files["file"]
        if image_file:
            image_path = "static/" + image_file.filename
            image_file.save(image_path)
            result = predict_cell(image_path)
            return render_template("index.html", prediction=result, image=image_file.filename)
    return render_template("index.html", prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
