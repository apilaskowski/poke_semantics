#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import sample, random, choice

g = nx.Graph()
min_size = 0.01
max_size = 0.3


def scale_func(x):
    x = x ** 5
    return x * (max_size - min_size) + min_size


edge_color = "magenta"
edge_width = 0.5
nn = 151
ne = int(nn ** 2 * 0.02)
imgs = []
for node_i in range(nn):
    g.add_node(node_i)
    imgs.append(mpimg.imread('sprites/{}.png'.format(node_i + 1)))
for edge_i in range(ne):
    x, y = sample(range(nn), 2)
    if (x, y) not in g.edges():
        g.add_edge(x, y, color=choice(["pink","magenta"]), weight=choice([2, 4]) / 8)

pos = nx.random_layout(g)

edges = g.edges()
edge_colors = [g[u][v]['color'] for u, v in edges]
edge_weights = [g[u][v]['weight'] for u, v in edges]

nx.draw(g, pos, node_size=0, edge_color=edge_colors, width=edge_weights)

# add images on edges
ax = plt.gca()
fig = plt.gcf()
label_pos = 0.5  # middle of edge, halfway between nodes
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.1  # this is the image size
for node in g.nodes():
    x, y = pos[node]
    xx, yy = trans((x, y))  # figure coordinates
    xa, ya = trans2((xx, yy))  # axes coordinates
    w = random()
    imsize = scale_func(w)
    a = plt.axes([xa - imsize / 2.0, ya - imsize / 2.0, imsize, imsize])
    a.imshow(imgs[node])
    # a.set_aspect('equal')
    a.axis('off')

plt.show()
# plt.savefig('/Pulpit/save.png')
