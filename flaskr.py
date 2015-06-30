from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import random

app = Flask(__name__)
app.config.from_object(__name__)
test_file = ["png/blue.png", "png/gray.png", "png/green.png","png/purple.png", "png/red.png", "png/white.png", "png/yellow.png"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_search')
def search():
    size = random.randint(1,20)
    list_result = []
    for x in xrange(0, size):
        list_result.append({
            "title": "Tou Xi Gua",
            "artist": "Xi Da Da",
            "director": "Jiang Da Da",
            "tag": "Tian Chao",
            "url": url_for("static", filename=test_file[random.randint(0,6)])
        })
    return jsonify(result=list_result)

if __name__ == '__main__':
    app.run(debug=True)

