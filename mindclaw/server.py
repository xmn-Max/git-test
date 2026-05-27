from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# 允许跨域
CORS(app)

@app.route("/chat")
def chat():

    user_msg = request.args.get("msg", "")

    return {
        "reply": "AI回复：" + user_msg
    }

app.run(debug=True)