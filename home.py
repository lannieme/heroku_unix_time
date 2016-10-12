from flask import Flask
import time
import sys

app = Flask(__name__)

@app.route('/')
def unixtime():
    return str(time.time()) + " seconds since Jan. 1st, 1970."

if __name__ == '__main__':
    app.run(port = sys.argv[1])
