from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# The 2026 Elite Prompt Database
PROMPT_DATABASE = {
    "tiktok": "Act as a Psychographics Expert. Create a 3-part viral script series about {topic}. Part 1: The Pattern Interrupt. Part 2: The Cognitive Dissonance. Part 3: The Dopamine Reward. Use short, punchy sentences designed for a 2026 attention span.",
    "email": "Write a 2026 'Invisible Selling' cold email regarding {topic}. Avoid all spam triggers. Use an 'Observation-Insight-Question' framework. Target a C-Suite executive with a value-first approach. Tone: Peer-to-Peer, not subordinate.",
    "business": "Act as a Silicon Valley VC. Conduct a SWOT analysis for a new venture in {topic}. Identify 3 'Blue Ocean' opportunities and a strategy to build a 'moat' around the business model to prevent AI replication."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    category = data.get('category')
    topic = data.get('topic', 'Emerging Tech')
    
    raw_prompt = PROMPT_DATABASE.get(category, "Protocol not found.")
    final_prompt = raw_prompt.format(topic=topic)
    
    return jsonify({"result": final_prompt})

if __name__ == '__main__':
    app.run(debug=True)
