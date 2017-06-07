#!/usr/bin/env python3

import requests
import pickle
import tqdm
import numpy as np

chart_file = open("types_chart.txt", "r")

types = [line.strip() for line in open("types.txt", "r")]

chart = np.loadtxt("types_chart.txt")

types_strengths = {}
for i, type_defend in enumerate(types):
    for j, type_attack in enumerate(types):
        types_strengths[(type_defend, type_attack)] = chart[i, j]


pokemons = [line.strip() for line in open("pokemon.csv", "r")]

print(pokemons)
