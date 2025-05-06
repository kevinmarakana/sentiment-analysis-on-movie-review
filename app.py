from flask import Flask, request, render_template
import joblib

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['review']
        text_vector = vectorizer.transform([text])
        prediction = model.predict(text_vector)[0]
        label = "Positive 😊" if prediction == 1 else "Negative 😞"
        return render_template("index.html", review=text, prediction=label)

if __name__ == '__main__':
    app.run(debug=True)
