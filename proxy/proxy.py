from flask import Flask, request, Response
import requests, time, threading, logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

MAIN_URL = "http://127.0.0.1:8001"
SPARE_URL = "http://127.0.0.1:8002"
BACKEND_URL = MAIN_URL
pinging = False

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    global pinging

    app.logger.info(f"Using backend: {BACKEND_URL}")
    method = request.method
    url = f"{BACKEND_URL}/{path}"

    headers = {key: value for key, value in request.headers if key != 'Host'}
    data = request.get_data()

    try:
        resp = requests.request(method, url, headers=headers, data=data)
        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Primary server failed: {e}")
        if not pinging:
            thread = threading.Thread(target=pingSpare)
            thread.start()
        return Response("Proxy error: server is down", status=502)

def pingSpare():
    global BACKEND_URL, pinging
    pinging = True

    while True:
        try:
            requests.get(f"{MAIN_URL}/monitor/ping/")
            BACKEND_URL = MAIN_URL
            app.logger.warning("MAIN server is up. Switching back.")
            break
        except:
            app.logger.warning("MAIN server is still down")

        try:
            requests.get(f"{SPARE_URL}/monitor/ping/")
            BACKEND_URL = SPARE_URL
            app.logger.warning("SPARE server is up. Switching to SPARE.")
            break
        except:
            app.logger.warning("SPARE server is also down")

        time.sleep(1)

    pinging = False

if __name__ == '__main__':
    app.run(port=8000)
