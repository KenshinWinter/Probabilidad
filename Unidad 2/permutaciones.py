# -*- coding: utf-8 -*-
"""Permutaciones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jr64j433YguDZVUUutijd0p0lUQqn8iu
"""

import math as mt
from itertools import permutations
from itertools import product
import numpy as np

mt.factorial(7)

mt.factorial(4)

5040/24

nombres = ["a", "b", "c", "d","e", "f", "g"]
n = len(nombres)
r = 3
Pr = mt.factorial(n) / (mt.factorial(n-r))

print("Aqui las permutaciones")
permutaciones_nombres = list(permutations(nombres, r))

# imprime las permutaciones
for permutacion in permutaciones_nombres:
    print(permutacion)