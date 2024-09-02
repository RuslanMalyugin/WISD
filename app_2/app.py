from flask import Flask, jsonify
import requests

app = Flask(__name__)
time_requests_count = 0


@app.route("/time", methods=["GET"])
def get_time():
    global time_requests_count
    time_requests_count += 1
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
        if response.status_code == 200:
            current_time = response.json().get("datetime")
            return jsonify({"current_time": current_time})
        else:
            return jsonify({"error": "Failed to fetch time"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/statistics", methods=["GET"])
def get_statistics():
    return jsonify({"time_requests_count": time_requests_count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
