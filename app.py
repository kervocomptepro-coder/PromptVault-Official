from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PROMPT_DATABASE = {
    "tiktok": "Act as a viral content creator. Write a 30-second TikTok script about {topic}. Include a hook that starts with 'Why nobody is talking about...' and end with a call to action.",
    "email": "Write a professional cold email regarding {topic}. Keep it under 100 words with a clear call to action.",
    "business": "Act as a business consultant. Provide 3 ways to monetize {topic} in 2026 with high profit margins."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    category = data.get('category')
    topic = data.get('topic', 'General')
    raw_prompt = PROMPT_DATABASE.get(category, "Select a category!")
    return jsonify({"result": raw_prompt.format(topic=topic)})

if __name__ == '__main__':
    app.run(debug=True)