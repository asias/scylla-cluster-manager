#!/usr/bin/env python3

import os
from utils import *


def gen_cmd(node, cluster_name, user, ip, ip_internal, seed, directory, num_tokens, dc, rack, prefer_local, shards, mem, fastboot):
    if fastboot:
        extra_args = "--skip-wait-for-gossip-to-settle 0 --ring-delay-ms 1 --compaction-enforce-min-threshold true --shadow-round-ms 1"
    else:
        extra_args = "--ring-delay-ms 5"

    if shards != "auto":
        extra_args += f" -c {shards} "

    if mem != "auto":
        extra_args += f" -m {mem}M "

    # FIXME: scylla {directory}/scylla/install.sh --nonroot --root {directory} does not work
    scylla_bin = f"/home/{user}/scylladb/bin/scylla"
    cmd = f'''
    cd {directory}
    mkdir -p conf
    touch conf/scylla.yaml
    echo "dc={dc}" > conf/cassandra-rackdc.properties
    echo "rack={rack} " >> conf/cassandra-rackdc.properties
    echo "prefer_local={prefer_local} " >> conf/cassandra-rackdc.properties
    {scylla_bin} --log-to-syslog 1 --logger-ostream-type stdout --log-to-stdout 1 {extra_args} --cluster-name {cluster_name} --options-file conf/scylla.yaml --seed-provider-parameters seeds={seed} --listen-address {ip_internal}  --rpc-address {ip_internal} --broadcast-address {ip} --broadcast-rpc-address {ip}  --start-native-transport true --start-rpc true --data-file-directories {directory}/data --commitlog-directory {directory}/commitlog --hints-directory {directory}/hints --view-hints-directory {directory}/view-hints --endpoint-snitch GossipingPropertyFileSnitch --num-tokens {num_tokens} --max-io-requests 50 --api-address {ip_internal} --developer-mode true --consistent-rangemovement false --experimental false --murmur3-partitioner-ignore-msb-bits 12 --enable-sstables-mc-format 1 --prometheus-address {ip_internal} --prometheus-port 9180 --prometheus-prefix scylla >{node}.log 2>&1 &
    echo $! > {node}.pid
    '''
    return cmd

def kill_scylla(node_name):
    cmd = f'''
    kill `cat {node_name}.pid`
    wait `cat {node_name}.pid`
    '''
    return cmd

def wait_port(ip, port, reason):
    cmd = f'''
    echo 'Wait for {ip} {port} to open for {reason} started'
    while ! nc -z {ip} {port}; do
        sleep 0.1
        done
    echo 'Wait for {ip} {port} to open for {reason} done'
    '''
    return cmd

def gen_cmds(cluster_name, user, nodes_info):
    dc="dc1"
    rack="rack1"
    prefer_local="true"
    msgs = []
    for info in nodes_info:
        ip = info[0]
        ip_internal = info[1]
        dc = info[2]
        rack = info[3]
        directory = info[4]
        seed = info[5]
        num_tokens = info[6]
        shards = info[7]
        mem = info[8]
        node_name = f"{CMD_FILE_PREFIX}.{ip}"
        msg = f"Created: node_name={node_name}, public_ip={ip}, private_ip={ip_internal}, dc={dc}, rack={rack}, directory={directory}, seed={seed}, num_tokens={num_tokens}, shards={shards}, mem={mem}"
        msgs.append(msg)
        with open(node_name, 'w', newline='\n') as out:
            cmd = gen_cmd(node=node_name, cluster_name=cluster_name, user=user, ip=ip, ip_internal=ip_internal, seed=ip, directory=directory, num_tokens=num_tokens, dc=dc, rack=rack, prefer_local=prefer_local, shards=shards, mem=mem, fastboot=True)
            cmd = out.write(cmd)

            cmd = wait_port(ip_internal, 9042, "prepare")
            cmd = out.write(cmd)

            cmd = kill_scylla(node_name=node_name)
            cmd = out.write(cmd)

            cmd = gen_cmd(node=node_name, cluster_name=cluster_name, user=user, ip=ip, ip_internal=ip_internal, seed=seed, directory=directory, num_tokens=num_tokens, dc=dc, rack=rack, prefer_local=prefer_local, shards=shards, mem=mem, fastboot=False)
            cmd = out.write(cmd)

            cmd = wait_port(ip_internal, 9042, "boot")
            cmd = out.write(cmd)
        os.chmod(node_name, 0o755)
    return msgs

if __name__ == '__main__':
    pass
