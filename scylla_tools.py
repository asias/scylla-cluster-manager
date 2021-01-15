#!/usr/bin/env python3

import requests
import json

def nodetool_status(ip, port=10000):
    r = requests.get(f'http://{ip}:{port}/gossiper/endpoint/live')
    live_nodes = set(json.loads(r.text))

    r = requests.get(f'http://{ip}:{port}/storage_service/host_id')
    host_ids = r.text
    host_ids = json.loads(host_ids)
    nodes = []
    for host_id in host_ids:
        ip = host_id['key']
        if ip in live_nodes:
            nodes.append({'ip':ip, 'host_id': host_id['value'], 'status' : 'UP'})
        else:
            nodes.append({'ip':ip, 'host_id': host_id['value'], 'status' : 'DOWN'})
    return nodes

if __name__ == '__main__':
    status = nodetool_status("127.0.0.1")
    for node in status:
        print(node)
