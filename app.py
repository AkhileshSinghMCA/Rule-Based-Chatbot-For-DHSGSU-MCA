from flask import Flask, render_template, request, jsonify
from spellchecker import SpellChecker
from chat import get_response

# Initialize the Flask app
app = Flask(__name__)

spell = SpellChecker()


@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the user input from the request
    text = request.get_json().get("message")
    
    # If no input is provided, return an error
    if not text:
        return jsonify({"error": "No input provided"}), 400

    # Perform spell check and correction
    corrected_words = [spell.correction(word) if spell.correction(word) else word for word in text.split()]
    corrected_text = " ".join(corrected_words)
    
    response = get_response(corrected_text)
   
    message = {"answer": response, "corrected_text": corrected_text}
    
    return jsonify(message)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
