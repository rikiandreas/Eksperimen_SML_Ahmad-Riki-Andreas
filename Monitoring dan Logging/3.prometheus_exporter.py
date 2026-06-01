
from flask import Flask, Response
import psutil
import time

app = Flask(__name__)

REQUEST_COUNT = 0

@app.route("/metrics")
def metrics():

    global REQUEST_COUNT

    start_time = time.time()

    REQUEST_COUNT += 1

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    latency = time.time() - start_time

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
