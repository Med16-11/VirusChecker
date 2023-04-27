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
    api_key = "ea2755cf0e5080ed3c674a1dd2d8b8ccc2703777ec4b410eb603a01b0bad3388"
    content = file.read()
    md5_sum = hashlib.md5()
    md5_sum.update(content)
    digest = md5_sum.hexdigest()

    vt = public_api(api_key)
    response = vt.get_file_report(digest)
    return render_template('results.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)


