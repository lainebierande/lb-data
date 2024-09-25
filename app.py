from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is my website."

if __name__ == '__main__':
    # Commit to Git
    os.system("git add .")
    os.system('git commit -m "Atjaunota"')
    os.system("git push -u origin main")

    try:
        app.run(debug=True, host='0.0.0.0', port=5000) 
    except Exception as e:
        print(f"Error: {e}")
