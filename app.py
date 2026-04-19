from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PROMPT_DATABASE = {
    "tiktok": "Analyze Objective: '{topic}'. Act as a Viral Media Architect. Script a 3-part series: 1. The Pattern Interrupt, 2. The Cognitive Dissonance, 3. The CTA. Use 2026 slang and punchy delivery.",
    "email": "Regarding '{topic}': Design a high-ticket cold email using the 'Invisible Selling' framework. Peer-to-peer tone, no fluff, value-first.",
    "vc_pitch": "Objective: '{topic}'. Act as a Series A Pitch Consultant. Outline a 10-slide deck focusing on the 'Unfair Advantage' and 'Market Inevitability'.",
    "moat": "Strategy for '{topic}': Identify 3 ways to build a defensible 'moat' around this business using proprietary data and AI-human loops.",
    "shadow": "Marketing Strategy: '{topic}'. Use Shadow-Work Psychographics. Target the prospect's 'suppressed desires' to create an irresistible pull toward the product.",
    "ghost": "Tone Protocol: '{topic}'. Act as a world-class Ghostwriter. Create a 5-post X/Twitter thread that positions the user as a thought leader in this space."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    category = data.get('category')
    topic = data.get('topic', 'Emerging Tech')
    raw_instruction = PROMPT_DATABASE.get(category, "Protocol Error.")
    return jsonify({"result": raw_instruction.replace("{topic}", topic)})

if __name__ == '__main__':
    app.run(debug=True)
