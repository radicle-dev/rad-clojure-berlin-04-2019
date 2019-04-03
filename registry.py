import requests
import argparse

def query(machine_id, expr):
    "Queries the given machine, with the provided expression"
    url = "http://localhost:8093/v0/machines/{0}/query".format(machine_id)
    requests.post(url, data = expr)

def send(machine_id, expr):
    "Send a new input to a machine"
    url = "http://localhost:8093/v0/machines/{0}/send".format(machine_id)
    requests.post(url, data = expr)

def list(machine_id):
    "List all projects of a machine"
    query(machine_id, "list")

def star(machine_id, project_id):
    "Star a project in a machine"
    submit(machine_id, "star")

parser = argparse.ArgumentParser(description='CLI for Radicle registry')
subparsers = parser.add_subparsers(dest='command')
list_parser = subparsers.add_parser('list')
star_parser = subparsers.add_parser('star')
star_parser.add_argument("project_id")

if __name__ == '__main__':
    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('subparser')](**kwargs)
