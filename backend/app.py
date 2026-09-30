from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze_grievance():
    data = request.json
    text = data.get('text')
    language = data.get('language')
    location = data.get('location')

    # In production, you would call the Google GenAI SDK / Gemini API here:
    # response = client.models.generate_content(model="gemini-2.5-flash", contents=...)

    # Mocked AI Backend Response matching your frontend expectation
    ai_result = {
        "status": "success",
        "translated_text": text, # In real app, translated via Gemini
        "category": "Public Infrastructure & Utilities",
        "urgency_score": "4.5 / 5 (High)",
        "location": location,
        "recommended_action": "Route to District Municipal Commissioner"
    }

    return jsonify(ai_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)