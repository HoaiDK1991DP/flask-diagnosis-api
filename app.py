from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from utils.diagnosis import match_symptoms

app = Flask(__name__)
CORS(app)

# Load dữ liệu bệnh
with open('data/diseases.json', 'r', encoding='utf-8') as f:
    DISEASES = json.load(f)

@app.route('/')
def home():
    return "API chẩn đoán bệnh đang chạy!"

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    user_symptoms = data.get('symptoms', [])
    result = match_symptoms(user_symptoms, DISEASES)
    return jsonify(result)

@app.route('/add', methods=['POST'])
def add_disease():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    symptoms = data.get('symptoms')

    if not name or not symptoms:
        return jsonify({"error": "Thiếu tên hoặc triệu chứng"}), 400

    new_disease = {
        "name": name,
        "description": description or "",
        "symptoms": symptoms
    }
    DISEASES.append(new_disease)

    # Ghi lại file
    with open('data/diseases.json', 'w', encoding='utf-8') as f:
        json.dump(DISEASES, f, ensure_ascii=False, indent=2)

    return jsonify({"message": "Đã thêm bệnh thành công!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

