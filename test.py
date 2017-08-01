from flask import Flask
app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
@app.route("/", methods=['POST'])
def show():
    return "hello world"
    

