from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)
time_requests_count = 0


@app.route("/time", methods=["GET"])
def get_time():
    global time_requests_count
    time_requests_count += 1
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"current_time": current_time})


@app.route("/statistics", methods=["GET"])
def get_statistics():
    return jsonify({"time_requests_count": time_requests_count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
