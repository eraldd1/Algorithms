import os
import sys
import random
from time import perf_counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLRS_DIR = os.path.join(BASE_DIR, "clrsPython")

#import the required folders for the functions only
for subfolder in ["Utility functions", "Chapter 20", "Chapter 22", "Chapter 10", "Chapter 6"]:
    sys.path.append(os.path.join(CLRS_DIR, subfolder))

from generate_random_graph import generate_random_graph
from dijkstra import dijkstra


def empirical_performance():
    #test run sizes of graph
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10000]

    #How many Dijkstra runs per graph size
    runs_per_size = 20

    #Probability that an edge exists between any pair of vertices
    edge_probability = 0.05

    #Edge weights
    min_weight = 1
    max_weight = 20

    random.seed(1337) #fixed seed for reproducibility

    print("Empirical Performance of Dijkstra on Random Graphs")
    print("N_vertices, average_time_per_dijkstra_seconds")

    for n in sizes:
        # Generate a random graph with n amount of vertices
        graph = generate_random_graph(
            card_V=n,
            edge_probability=edge_probability,
            by_adjacency_lists=True,
            directed=False,
            weighted=True,
            min_weight=min_weight,
            max_weight=max_weight,
        )

        total_time = 0.0

        for i in range(runs_per_size):
            #Choose a random source vertex
            s = random.randrange(n)

            #measure the time dijkstra needs to run
            t0 = perf_counter()
            d, pi = dijkstra(graph, s)
            t1 = perf_counter()

            total_time += (t1 - t0)

        avg_time = total_time / runs_per_size
        print(f"{n}, {avg_time:.9f}")


if __name__ == "__main__":
    empirical_performance()
