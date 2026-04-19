from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PROMPT_DATABASE = {
    "tiktok": "Analyze the objective: '{topic}'. Act as a Senior Viral Strategist. Construct a high-retention script that ignores the obvious. Part 1: Start with a 'Visual Hook' that lasts 1.5 seconds. Part 2: Address the hidden desire behind {topic}. Part 3: Use a rapid-fire editing style prompt. Tone: Authority, 2026 Trend-Setter.",
    "email": "Regarding '{topic}': Create a high-ticket outreach sequence. Step 1: Identify the prospect's biggest pain point related to this topic. Step 2: Present a 'Unique Mechanism' solution. Step 3: Low-friction CTA. Style: Minimalist, Ultra-Professional.",
    "business": "Strategic Deep Dive on '{topic}'. Conduct a market analysis for 2026. Find the 'Gap in the Matrix'—where are the competitors failing? Propose a business model that uses AI automation to remove 90% of overhead while maintaining 100% quality."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    category = data.get('category')
    topic = data.get('topic', 'General Strategy')
    
    # This logic makes it smarter
    raw_instruction = PROMPT_DATABASE.get(category)
    final_output = raw_instruction.replace("{topic}", topic)
    
    return jsonify({"result": final_output})

if __name__ == '__main__':
    app.run(debug=True)
