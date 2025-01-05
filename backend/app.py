from flask import Flask, request, jsonify, render_template
from blockchain.contract_interaction import vote, get_votes

app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# API to submit a vote
@app.route('/vote', methods=['POST'])
def vote_route():
    data = request.get_json()
    candidate = data.get('candidate')
    if not candidate:
        return jsonify({"error": "Candidate name is required"}), 400
    
    tx_hash = vote(candidate)
    return jsonify({"message": "Vote submitted successfully", "transaction": tx_hash})

# API to fetch votes for a candidate
@app.route('/results', methods=['GET'])
def results():
    candidate = request.args.get('candidate')
    if not candidate:
        return jsonify({"error": "Candidate name is required"}), 400
    
    votes = get_votes(candidate)
    return jsonify({"candidate": candidate, "votes": votes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
