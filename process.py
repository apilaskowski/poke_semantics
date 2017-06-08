#!/usr/bin/env python3

import requests
import pickle
import tqdm
import numpy as np
from collections import namedtuple
from collections import Counter

chart_file = open("types_chart.txt", "r")

types = [line.strip() for line in open("types.txt", "r")]

chart = np.loadtxt("types_chart.txt")

types_strengths = {}
for i, type_attack in enumerate(types):
    for j, type_defend in enumerate(types):
        types_strengths[(type_attack, type_defend)] = chart[i, j]


pokemons_file = [line.strip() for line in open("pokemon.csv", "r")]

Pokemon = namedtuple('Pokemon', ['id', 'name', 'type'])

pokemons = []

cnt = Counter()

for pokemon_line in pokemons_file:
    tab = pokemon_line.split(';')
    if tab[1].startswith("#"):
        if not tab[2] in cnt:
            cnt[tab[2]] += 1
            pokemons.append(Pokemon(tab[1], tab[2], tuple(tab[4:])))
    elif tab[0].startswith("#"):
        if not tab[2] in cnt:
            cnt[tab[2]] += 1
            pokemons.append(Pokemon(tab[0], tab[1], tuple(tab[3:])))

print(len(pokemons))

graph = {}

for attacker in pokemons:
    for defender in pokemons:
        ratio = 1.0
        for a_ptype in attacker[2]:
            for d_ptype in defender[2]:
                ratio *= types_strengths[a_ptype, d_ptype]
        graph[(attacker, defender)] = ratio

perfect_graph = {}

good_edge = 0
for attacker in pokemons:
    for defender in pokemons:
        if graph[attacker, defender] > 1:
            good_edge += 1
            perfect_graph[attacker, defender] = graph[attacker, defender]
