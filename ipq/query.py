from flask import (
        Blueprint, flash, render_template, request, g
        )
from ipq.db import get_db
from netaddr import IPNetwork

bp = Blueprint('query', __name__)

@bp.route('/', methods=('GET', 'POST'))
def query():
    if request.method == 'POST':
        ip = request.form['ip']
        db = get_db()
        error = None
        g.ip = ip
        g.subnet = None

        if not ip:
            error = 'IP address is required.'
        networks = db.execute('SELECT network_id, cidr FROM network').fetchall()
        for net in networks:
            network = IPNetwork(f"{net[0]}/{net[1]}")
            if ip in network:
                print(f"{ip} is in the {network} subnet")
                g.subnet = str(network)

        flash(error)

    return render_template('query/query.html')
