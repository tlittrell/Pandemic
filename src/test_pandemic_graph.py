import networkx as nx

from src.game_graph import edges


def test_graph_degrees(g):
    g = nx.Graph()
    for i, cities in enumerate(edges):
        g.add_edge(cities[0], cities[1])

    assert g.degree('Lima') == 4
    assert g.degree('Mexico City') == 5
    assert g.degree('Manila') == 5
    assert g.degree('Taipei') == 4
    assert g.degree('Osaka') == 2
    assert g.degree('Tokyo') == 4
    assert g.degree('Seoul') == 3
    assert g.degree('Ho Chi Minh City') == 4
    assert g.degree('Hong Kong') == 6
    assert g.degree('Shanghai') == 5
    assert g.degree('Beijing') == 2
    assert g.degree('Sydney') == 3
    assert g.degree('Jakarta') == 4
    assert g.degree('Bangkok') == 4
    assert g.degree('Mumbai') == 3
    assert g.degree('Chennai') == 4
    assert g.degree('Kolkata') == 4
    assert g.degree('Delhi') == 5
    assert g.degree('Karachi') == 4
    assert g.degree('Tehran') == 4
    assert g.degree('Riyadh') == 3
    assert g.degree('Baghdad') == 4
    assert g.degree('Moscow') == 3
    assert g.degree('Lagos') == 3
    assert g.degree('Kinshasa') == 3
    assert g.degree('Khartoum') == 4
    assert g.degree('Johannesburg') == 3
    assert g.degree('Cairo') == 5
    assert g.degree('Istanbul') == 6
    assert g.degree('Algiers') == 4
    assert g.degree('St Petersburg') == 3
    assert g.degree('Milan') == 3
    assert g.degree('Essen') == 4
    assert g.degree('Atlanta') == 3
    assert g.degree('Chicago') == 5
    assert g.degree('Montreal') == 3
    assert g.degree('Washington') == 4
    assert g.degree('Los Angeles') == 5
    assert g.degree('San Francisco') == 4
    assert g.degree('Miami') == 4
    assert g.degree('Bogota') == 5
    assert g.degree('Santiago') == 2
    assert g.degree('Sao Paulo') == 4
    assert g.degree('Buenos Aires') == 4
    assert g.degree('New York') == 4
    assert g.degree('London') == 4
    assert g.degree('Madrid') == 5
    assert g.degree('Paris') == 5
