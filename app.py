from flask import Flask, request, render_template, jsonify
import ollama

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'response': 'No prompt provided.'})

    try:
        output = ollama.chat(model='tinyllama', messages=[{"role": "user", "content": prompt}])
        response = output['message']['content']
    except Exception as e:
        response = f"Error: {str(e)}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
