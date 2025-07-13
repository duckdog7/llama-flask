from flask import Flask, request, render_template_string
import ollama

app = Flask(__name__)

# Basic HTML page template for chatting
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Talk to TinyLLaMA</title>
</head>
<body>
    <h1>Talk to TinyLLaMA</h1>
    <form method="post">
        <textarea name="prompt" rows="4" cols="50" placeholder="Ask something..."></textarea><br>
        <input type="submit" value="Submit">
    </form>
    {% if response %}
        <h3>Response:</h3>
        <p>{{ response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def chat():
    response = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        output = ollama.chat(model='tinyllama', messages=[{"role": "user", "content": prompt}])
        response = output['message']['content']
    return render_template_string(HTML_PAGE, response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
