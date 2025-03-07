from flask import Flask, Response, render_template
from sse import sse_counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sse/counter')
def counter():
    return Response(sse_counter(), mimetype='text/event-stream')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
