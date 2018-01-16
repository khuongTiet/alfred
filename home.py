from flask import Flask, render_template, request, Response
import json
import main
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    target_link = request.form['target']
    return render_template('results.html', target = target_link, downloads = main.find_files_json(target_link))

if __name__ == '__main__':
    app.run(debug=True)
