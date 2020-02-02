import sys
from flask import Flask, escape, request
from netaddr import IPNetwork

"""
# this first piece to acquire the data will change w/ some given asset list
ip = sys.argv[1]
networks_file = open('assets.txt')
networks = [IPNetwork(net) for net in networks_file.read().split('\n') if net]

for net in networks:
    if ip in net:
        print(f"The IP {ip} is in {net}")

networks_file.close()

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.args.get("ip", "192.168.1.1")
    return f'Hello, {escape(ip)}!'
"""
