import app
from flask import render_template


@app.route('/resume')
def resume():
    return render_template('Resume.html')
