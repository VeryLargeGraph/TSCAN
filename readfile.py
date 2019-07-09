# -*- coding: utf-8 -*-
import networkx as nx
import random


def Graph(path):
    G = nx.Graph()
    for line in open(path):
        # print line
        if line.find('#') and line.find('%') < 0 and line != '\n':
            line=line.strip('\n').split('\t')
            if int(line[0]) == int(line[1]):
                continue
            # print line
            G.add_edge(int(line[0]), int(line[1]))
    G.add_node(0)
    return G


def tGraph(path):
    G = nx.Graph()
    for line in open(path):
        if line.find('#') and line.find('%') < 0 and line != '\n':
            line = line.strip('\n').split('\t')
            if int(line[0]) == int(line[1]):
                continue

            if G.has_edge(int(line[0]), int(line[1])):
                if int(line[2]) not in G.edges[int(line[0]), int(line[1])]['t']:
                    G.edges[int(line[0]), int(line[1])]['t'].append(int(line[2]))
                    # print(int(line[0]), int(line[1]) ,G.edges[int(line[0]), int(line[1])])
            else:
                G.add_edge(int(line[0]), int(line[1]), t=[int(line[2])])
    return G


def tSubgraph(path, now, theta, i):
    G = nx.Graph()
    first_time = -1
    for line in open(path):
        if line.find('#') < 0 and line.find('%') < 0 and line != '\n':
            line = line.strip('\n').split('\t')
            if int(line[0]) == int(line[1]):
                continue
            if int(float(line[2])) > now - i * theta  and int(float(line[2])) <= now:
                G.add_edge(int(line[0]), int(line[1]), time=int((line[2])))

    return G


def format(path):
    file_object = open(path + '.new', 'w')
    maxtime = 0
    mintime = 1000000
    for line in open(path):
        if line.find('#') and line.find('%') < 0 and line != '\n':
            line = line.strip('\n').split(' ')
            newline = [line[0], line[1], line[4]]
            # print line
            time = (int(newline[2])-1162422000)/3600/24
            if time > maxtime:
                maxtime = time
            if time < mintime:
                mintime = time

            newline[2] = str(time)
            newline = "\t".join(newline) + '\n'
            # print(newline)
            file_object.write(newline)

    print(maxtime,mintime)
    file_object.close()


if __name__ == '__main__':
    format("c:\\dataset\\flickr")