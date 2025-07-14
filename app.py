from flask import Flask, request, render_template_string
import ollama

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Auto-reload templates when updated

@app.route('/', methods=['GET', 'POST'])
def chat():
    response = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        output = ollama.chat(model='tinyllama', messages=[{"role": "user", "content": prompt}])
        response = output['message']['content']
    return render_template("index.html", response=response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
