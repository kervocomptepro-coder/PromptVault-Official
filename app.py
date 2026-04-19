from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    category = data.get('category', 'tiktok').replace('PREMIUM: ', '')
    topic = data.get('topic', 'General Intelligence')
    entropy = data.get('entropy', 'stable')

    # Intelligence Frameworks
    templates = {
        "tiktok": f"FRAMEWORK: Viral Architect\nTOPIC: {topic}\n\n1. HOOK: Pattern interrupt involving {topic}.\n2. RETENTION: Reveal the 'hidden' truth about this industry.\n3. CTA: Direct to bio for full protocol access.",
        
        "email": f"FRAMEWORK: Sales Logic\nTOPIC: {topic}\n\nSubject: The {topic} bottleneck you're ignoring.\n\nBody: Most treat {topic} as a surface issue. Here is the asymmetrical fix...",
        
        "vc_pitch": f"PROTOCOL: VC Funding Pitch\nPROJECT: {topic}\n\n- MARKET GAP: Why current {topic} solutions fail.\n- MOAT: Proprietary data loops around the {topic} sector.\n- EXIT: 24-month high-value acquisition strategy.",
        
        "moat": f"STRATEGY: Strategic Moat Analysis\nCORE: {topic}\n\nIdentify network effects and high switching costs available in {topic}. Build a walled garden around the user base.",
        
        "shadow": f"PSYCHE: Shadow-Work Marketing\nTARGET: {topic}\n\nIdentify the hidden insecurity the customer has regarding {topic}. Offer the 'light' solution through your service.",
        
        "whale": f"ANALYSIS: Crypto Whale Protocol\nASSET: {topic}\n\nIdentify the supply-side shock for {topic}. Analyze whale wallet accumulation patterns for the 2026 cycle."
    }

    result = templates.get(category, "System error: Logic stream corrupted.")
    
    # Chaos Modifier
    if entropy == "chaotic":
        result = f"[OVERRIDE ACTIVE]\n\n{result.upper().replace('.', ' !!!')}"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
