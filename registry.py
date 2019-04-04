#!/usr/bin/env python3

import requests
import argparse

def mk_req(typ, machine_id, expr):
    """ Make a request to a machine.
    `typ` should be one of "send" or "query"
    """
    url = "http://localhost:8909/v0/machines/{0}/{1}".format(machine_id, typ)
    res = requests.post(url, data = expr)
    if not(res.status_code == 200):
        exit("Machine did not like request")
    else:
        res

def list(**kw):
    "List all projects of a machine"
    print(mk_req("query", kw["machine_id"], "list"))

def star(**kw):
    "Star a project in a machine"
    mk_req("send", kw["machine_id"], "star")

parser = argparse.ArgumentParser(description='CLI for Radicle registry')
subparsers = parser.add_subparsers(dest='command')
list_parser = subparsers.add_parser('list')
list_parser.add_argument("machine_id", type=str)

list_parser.set_defaults(func=list)
star_parser = subparsers.add_parser('star')
star_parser.add_argument("project_id")


args = parser.parse_args()
args.func(**vars(args))
