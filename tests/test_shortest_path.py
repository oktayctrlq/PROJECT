from sp211 import dijkstra

def test_dijkstra_basic():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 1, 'D': 5},
        'C': {'D': 8, 'E': 10},
        'D': {'E': 2, 'F': 6},
        'E': {'F': 2},
        'F': {},
    }
    distances, previous = dijkstra(graph, 'A')
    assert distances['F'] == 13  # A->B->D->E->F en kısa yol


