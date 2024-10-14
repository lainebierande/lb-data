from flask import Flask, render_template
import os

app = Flask(__name__)

# Route that renders index.html
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/matematika')
def matemātika():
    return render_template('matematika.html')

@app.route('/latviesuvaloda')
def latviesuvaloda():
    return render_template('latviesuvaloda.html')

@app.route('/angluvaloda')
def angluvaloda():
    return render_template('angluvaloda.html')

@app.route('/dabaszinibas')
def dabaszinibas():
    return render_template('dabaszinibas.html')



if __name__ == '__main__':
    # Commit to Git
    os.system("git add .")
    os.system('git commit -m "new changes"')
    os.system("git push -u origin main") 
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5001) 
    except Exception as e:
        print(f"Error: {e}")