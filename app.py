from flask import Flask, request, jsonify
from utils.parser import parse_resume
from utils.scorer import score_resume

app = Flask(__name__)

@app.route('/')
def index():
    return "📄 SmartResumeScore API is running!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['resume']
    text = parse_resume(file)
    result = score_resume(text)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
