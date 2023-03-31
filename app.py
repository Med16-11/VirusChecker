from flask import Flask, render_template, request
import sys
import hashlib
import json
from virus_total_apis import PublicApi as public_api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    file = request.files['file']
    api_key = "<your_api_key_here>"
    content = file.read()
    md5_sum = hashlib.md5()
    md5_sum.update(content)
    digest = md5_sum.hexdigest()

    vt = public_api(api_key)
    response = vt.get_file_report(digest)
    return render_template('results.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)


