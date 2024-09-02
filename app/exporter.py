from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route("/metrics")
def metrics():
    try:
        response = requests.get("http://web-app:5000/statistics")
        data = response.json()
        request_count = data.get("time_requests_count", 0)

        prometheus_metrics = f"""
# HELP request_count Number of requests to /time endpoint
# TYPE request_count counter
request_count {request_count}
"""
        return Response(prometheus_metrics, mimetype="text/plain")
    except Exception as e:
        return Response(
            f"Error fetching metrics: {e}", status=500, mimetype="text/plain"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9100)
