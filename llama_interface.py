import subprocess

def query_llama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama"],
            input=prompt.encode(),
            capture_output=True,
            timeout=30
        )
        return result.stdout.decode()
    except subprocess.TimeoutExpired:
        return "Timed out waiting for TinyLLaMA."
    except Exception as e:
        return f"Error: {str(e)}"
