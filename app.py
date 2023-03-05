from flask import Flask, request, jsonify, render_template
from chatgpt import chatgpt_request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    prompt = request.json.get('promptValue')
    response = chatgpt_request(prompt)
    print(response)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
