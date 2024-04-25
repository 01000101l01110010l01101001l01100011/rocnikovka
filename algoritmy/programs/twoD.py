from random import random  # Importuje funkci random pro generování náhodných čísel
from math import dist  # Importuje funkce dist z modulu math pro výpočty
from networkx import Graph, neighbors  # Importuje třídu Graph a funkci neighbors z modulu networkx pro práci s grafy
from itertools import combinations
import numpy as np
def create_points(n):
  points = {}  # Inicializuje prázdný slovník pro ukládání bodů
  set_points = set()  # Inicializuje prázdnou množinu pro ukládání unikátních bodů
  for i in range(n):
    x, y = random()*10, random()*10  # Generuje náhodné souřadnice bodu v rozsahu 0-10
    while (x, y) in points.values():  # Kontroluje, zda již existuje bod se stejnými souřadnicemi
      x, y = random()*10, random()*10  # Pokud ano, generuje nové souřadnice
    points[i] = (x, y)  # Přidá bod do slovníku
    set_points.add((x, y))  # Přidá bod do množiny
  return points, set_points  # Vrací slovník bodů a množinu bodů

def find_path(G:Graph, start, end):
  min_path = None, None, None, float("inf")  # Proměnnou pro nejkratší cestu s nekonečnou vzdáleností
  for x in neighbors(G, start) :  # Prochází sousedy počátečního bodu v grafu G
    path = G.get_edge_data(start, x)["weight"] + G.get_edge_data(end, x)["weight"]  # Spočítá vzdálenost cesty přes aktuálního souseda
    if float(min_path[3]) > path:  # Pokud je nová cesta kratší než dosavadní nejkratší cesta
      min_path = start, x, end, path  # Aktualizuje nejkratší cestu
  return min_path  # Vrací nejkratší cestu

def algorithmtwo(V:np.array):
  G = Graph()  # Prázdný graf
  subsets = list(combinations(V, 2)) # Všchny dvouprvkové podmnožiny V
  for edge in subsets: # Pro hranu v subsets.
    G.add_weighted_edges_from([((edge[0][0], edge[0][1]), (edge[1][0], edge[1][1]), dist(edge[0], edge[1]))])  # Přidá hranu edge do grafu G s její váhou.

  min_triangle = None  # Proměnná pro nejmenší trojúhelník
  min_triangle_weight = float("inf")  # Proměnná pro váhu nejmenšího trojúhelníku s nekonečnou hodnotou
  for edge in G.edges():  # Prochází hrany v seznamu hran
    edge_weight = G.get_edge_data(edge[0], edge[1])["weight"]  # Získá váhu hrany edge
    G.remove_edge(edge[0], edge[1])  # Odebere hranu z grafu
    u, j, v, weight= find_path(G, edge[0], edge[1])  # Najde nejkratší cestu mezi body edge[0] a edge[1]
    if (v[1]-u[1])*(j[0]-u[0]) == (j[1]-u[1])*(v[0]-u[0]):  # Pokud body u, j, v leží na jedné přímce
      if dist(u, j) > dist(u, v):  # Pokud je vzdálenost mezi body u a j větší než vzdálenost mezi body u a v
        G.remove_edge(u, j)  # Odebere hranu mezi body u a j
      elif dist(j, v) > dist(u, v):  # Pokud je vzdálenost mezi body j a v větší než vzdálenost mezi body u a v
        G.remove_edge(v, j)  # Odebere hranu mezi body v a j
      else:
        continue  # Pokračuje na další iteraci cyklu
    elif weight + edge_weight < min_triangle_weight:  # Pokud je váha cesty plus váha hrany menší než váha nejmenšího trojúhelníku
      min_triangle = (u, j, v)  # Aktualizuje nejmenší trojúhelník
      min_triangle_weight = weight + edge_weight  # Aktualizuje váhu nejmenšího trojúhelníku
    G.add_weighted_edges_from([(u, v, dist(u, v))])  # Přidá hranu u, v zpatky do grafu s její váhou

  return min_triangle, min_triangle_weight  # Vrací nejmenší trojúhelník a jeho váhu