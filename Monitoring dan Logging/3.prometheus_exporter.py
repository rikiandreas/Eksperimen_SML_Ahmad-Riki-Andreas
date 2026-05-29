from flask import Flask, Response
import random

app = Flask(__name__)

REQUEST_COUNT = 0

@app.route("/metrics")
def metrics():

    global REQUEST_COUNT

    REQUEST_COUNT += 1

    cpu_usage = random.randint(1, 100)
    ram_usage = random.randint(1, 100)
    latency = random.uniform(0.1, 0.9)

    return Response(f"""
# HELP http_requests_total Total HTTP Requests
# TYPE http_requests_total counter
http_requests_total {REQUEST_COUNT}

# HELP system_cpu_usage CPU Usage
# TYPE system_cpu_usage gauge
system_cpu_usage {cpu_usage}

# HELP system_ram_usage RAM Usage
# TYPE system_ram_usage gauge
system_ram_usage {ram_usage}

# HELP request_latency_seconds Request latency
# TYPE request_latency_seconds gauge
request_latency_seconds {latency}
""", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
