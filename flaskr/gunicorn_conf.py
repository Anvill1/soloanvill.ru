import multiprocessing

bind = '0.0.0.0:8095'
workers = 4
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 3
