from flask import Flask, Response
import random

app = Flask(__name__)

REQUEST_COUNT = 0
LATENCY = 0.0

@app.route("/metrics")
def metrics():
    global REQUEST_COUNT, LATENCY

    REQUEST_COUNT += 1
    LATENCY = random.uniform(0.1, 0.9)

    return Response(f"""
# HELP request_count total request
# TYPE request_count counter
request_count {REQUEST_COUNT}

# HELP latency request latency
# TYPE latency gauge
latency {LATENCY}
""", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
