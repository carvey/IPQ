import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from netaddr import IPNetwork

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('load-db')
@click.argument('network_path')
@with_appcontext
def load_db(network_path):
    network_file = open(network_path)
    networks = [(str(IPNetwork(net).network), IPNetwork(net).prefixlen) for net in network_file.read().split('\n') if net] 
    network_file.close()

    db = get_db()
    c = db.cursor()
    for net in networks:
        c.execute(f"INSERT INTO network (network_id, cidr) VALUES (?, ?)", net)

    db.commit()
    db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_db)

