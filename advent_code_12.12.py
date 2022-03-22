# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:31:10 2021

@author: Niky
"""

def parse_input(fh):
    with open(f"{fh}.txt") as f:
        lines  = [x.strip("\n") for x in f.readlines()]
    return lines

def find_connections(lines):
    connections = {}
    for line in lines:
        key, val = line.split("-")
        connections.setdefault(key,[] )
        connections[key].append(val)
    for line in lines:
        key, val = line.split("-")
        if val != "end":
            connections.setdefault(val,[] )
            connections[val].append(key)
    return connections

def parse_nodes(path,connections, max_visit):
    visits = {}
    for e in path:
        visits.setdefault(e, 0)
    end_node = "end"
    paths = []
    node = path[-1]
    for node in path:
        visits[node]+=1
    reached = False
    for e in visits.keys():
        if visits[e] == max_visit and e.islower():
            reached = True
    nbs = connections[node]
    for nb in nbs:
        if nb == "start":
            continue
        if nb.islower() and nb != "end":
            if reached == True:
                try:
                    if visits[nb] >= 1:
                        continue
                except KeyError:
                    visits[node]=1
            else:
                try:
                    if visits[nb] >= max_visit:
                        continue
                except KeyError:
                    visits[node]=1
        update_path = path+[nb]
        if nb==end_node:
            paths.append(update_path)
        else:
            paths +=parse_nodes(update_path,connections, max_visit)
    return paths

connections = find_connections(parse_input("day_12"))
paths = ["start"]   
paths_1 = parse_nodes(paths,connections, 1)        
print(f"Result one: {len(paths_1)}")
paths_2 = parse_nodes(paths,connections, 2)
print(f"Result two: {len(paths_2)}")

