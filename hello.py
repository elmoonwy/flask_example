from flask import Flask, url_for, render_template, request
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/user/<username>')
def profile(username): pass

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        pass
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

# with app.test_request_context():
# 	print url_for('index')
# 	print url_for('login')
# 	print url_for('login', next='/')
# 	print url_for('profile', username='John Doe')
# 	print url_for('static', filename="test.css")
