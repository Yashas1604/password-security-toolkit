from flask import Flask, render_template, request, jsonify
from modules.strength_analyzer import analyze_strength
from modules.brute_force import hash_password, brute_force_attack, dictionary_attack
from modules.dictionary_generator import generate_dictionary
from modules.hash_extractor import extract_simulated_hashes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.form['password']
    result = analyze_strength(password)
    return jsonify(result)

@app.route('/generate', methods=['POST'])
def generate():
    words = request.form['words'].split(',')
    result = generate_dictionary([w.strip() for w in words])
    return jsonify(result)

@app.route('/hashextract', methods=['POST'])
def hashextract():
    username = request.form['username']
    password = request.form['password']
    result = extract_simulated_hashes({username: password})
    return jsonify(result)

@app.route('/bruteforce', methods=['POST'])
def bruteforce():
    password = request.form['password']
    target_hash = hash_password(password)
    result = brute_force_attack(target_hash, max_length=4)
    return jsonify(result)

@app.route('/dictionary', methods=['POST'])
def dictionary():
    password = request.form['password']
    target_hash = hash_password(password)
    result = dictionary_attack(target_hash, "wordlist.txt")
    return jsonify(result)

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)