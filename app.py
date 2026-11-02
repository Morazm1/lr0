import os
import pwd
import socket
import time

import redis
from flask import Flask, jsonify

app = Flask(__name__)

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))


def connect_redis(attempts=30, delay=1.0):
    """Ждём, пока redis поднимется, чтобы контейнер не падал сразу."""
    last_error = None
    for _ in range(attempts):
        try:
            client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_timeout=2)
            client.ping()
            return client
        except redis.RedisError as exc:
            last_error = exc
            time.sleep(delay)
    raise RuntimeError(f"Redis недоступен по адресу {REDIS_HOST}:{REDIS_PORT}: {last_error}")


client = connect_redis()


@app.route("/")
def index():
    visits = client.incr("visits")
    return f"<h1>ЛР0: Flask + Redis</h1><p>Визитов: {visits}</p>"


@app.route("/whoami")
def whoami():
    entry = pwd.getpwuid(os.getuid())
    return jsonify(
        user=entry.pw_name,
        uid=os.getuid(),
        gid=os.getgid(),
        host=socket.gethostname(),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
