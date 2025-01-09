import os

bind = f"0.0.0.0:{os.environ.get('PORT', 10000)}"
workers = 2
threads = 4
timeout = 120
keepalive = 120
worker_class = "sync"
worker_connections = 1000
max_requests = 0
max_requests_jitter = 0

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# SSL
keyfile = None
certfile = None

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Server hooks
def on_starting(server):
    print("Starting Gunicorn server...")

def on_exit(server):
    print("Shutting down Gunicorn server...")