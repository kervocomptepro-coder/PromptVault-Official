from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PROMPT_DATABASE = {
    "tiktok": "Act as a Content Architect. Objective: '{topic}'. Strategy: {entropy_mod}. Create a high-retention script series with psychological hooks.",
    "email": "Regarding '{topic}': Build a cold-outreach system using '{entropy_mod}' logic. Target: High-value prospects. Tone: Peer-to-Peer.",
    "vc_pitch": "Objective: '{topic}'. VC Pitch Protocol. Focus on 'Market Inevitability' and 'Unit Economics'.",
    "moat": "Strategic Deep-Dive: '{topic}'. Identify 3 proprietary data loops to prevent competitors from copying the business model.",
    "shadow": "Shadow-Work Protocol: '{topic}'. Analyze the hidden pain points of the target audience and weaponize them into a marketing angle.",
    "whale": "Crypto Whale Intel: '{topic}'. Act as a Lead Analyst. Identify the asymmetrical upside for this project in the 2026 bull cycle."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    category = data.get('category', 'tiktok').replace('PREMIUM: ', '')
    topic = data.get('topic', 'Alpha Protocol')
    entropy = data.get('entropy', 'stable')
    
    entropy_mod = "highly logical and data-driven" if entropy == "stable" else "experimental, disruptive, and chaotic"
    
    raw_instruction = PROMPT_DATABASE.get(category, "Protocol Error.")
    final_output = raw_instruction.replace("{topic}", topic).replace("{entropy_mod}", entropy_mod)
    
    return jsonify({"result": final_output})

if __name__ == '__main__':
    app.run(debug=True)
