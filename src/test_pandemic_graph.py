import networkx as nx

from src.game_graph import edges


class TestGraph(object):
    def setup_method(self):
        self.g = nx.Graph()
        for i, cities in enumerate(edges):
            self.g.add_edge(cities[0], cities[1])

    def test_graph_degrees(self):
        assert self.g.degree("Lima") == 4
        assert self.g.degree("Mexico City") == 5
        assert self.g.degree("Manila") == 5
        assert self.g.degree("Taipei") == 4
        assert self.g.degree("Osaka") == 2
        assert self.g.degree("Tokyo") == 4
        assert self.g.degree("Seoul") == 3
        assert self.g.degree("Ho Chi Minh City") == 4
        assert self.g.degree("Hong Kong") == 6
        assert self.g.degree("Shanghai") == 5
        assert self.g.degree("Beijing") == 2
        assert self.g.degree("Sydney") == 3
        assert self.g.degree("Jakarta") == 4
        assert self.g.degree("Bangkok") == 4
        assert self.g.degree("Mumbai") == 3
        assert self.g.degree("Chennai") == 4
        assert self.g.degree("Kolkata") == 4
        assert self.g.degree("Delhi") == 5
        assert self.g.degree("Karachi") == 4
        assert self.g.degree("Tehran") == 4
        assert self.g.degree("Riyadh") == 3
        assert self.g.degree("Baghdad") == 4
        assert self.g.degree("Moscow") == 3
        assert self.g.degree("Lagos") == 3
        assert self.g.degree("Kinshasa") == 3
        assert self.g.degree("Khartoum") == 4
        assert self.g.degree("Johannesburg") == 3
        assert self.g.degree("Cairo") == 5
        assert self.g.degree("Istanbul") == 6
        assert self.g.degree("Algiers") == 4
        assert self.g.degree("St Petersburg") == 3
        assert self.g.degree("Milan") == 3
        assert self.g.degree("Essen") == 4
        assert self.g.degree("Atlanta") == 3
        assert self.g.degree("Chicago") == 5
        assert self.g.degree("Montreal") == 3
        assert self.g.degree("Washington") == 4
        assert self.g.degree("Los Angeles") == 5
        assert self.g.degree("San Francisco") == 4
        assert self.g.degree("Miami") == 4
        assert self.g.degree("Bogota") == 5
        assert self.g.degree("Santiago") == 2
        assert self.g.degree("Sao Paulo") == 4
        assert self.g.degree("Buenos Aires") == 4
        assert self.g.degree("New York") == 4
        assert self.g.degree("London") == 4
        assert self.g.degree("Madrid") == 5
        assert self.g.degree("Paris") == 5
