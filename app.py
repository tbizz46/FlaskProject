from flask import Flask, render_template
import os

# Explicitly set the templates directory
app = Flask(__name__, template_folder=os.path.abspath("templates"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')  # Ensure the filename matches exactly

if __name__ == '__main__':
    app.run(debug=True)
