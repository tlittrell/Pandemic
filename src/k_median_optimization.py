from collections import namedtuple

import networkx as nx
from pyomo.environ import *
from pyomo.opt import SolverFactory


def optimize_station_placement(game_graph, max_facilities):
    cities = list(game_graph.nodes)

    m = ConcreteModel()
    m.x = Var(cities, cities, within=Binary)
    m.y = Var(cities, within=Binary)

    # each city must be assigned to one and only one research facility
    def city_assigned_to_research_station(model, city):
        return sum(model.x[possible_facility, city] for possible_facility in cities) == 1

    m.each_city_assigned = Constraint(cities, rule=city_assigned_to_research_station)

    # can only assign a city to a research station if that station is active
    def assign_only_if_active(model, possible_facility, city):
        return m.x[possible_facility, city] <= m.y[possible_facility]

    m.active_facilities_only = Constraint(cities, cities, rule=assign_only_if_active)

    # limit the number of facilities
    m.max_facilities = Constraint(expr=sum(m.y[possible_facility] for possible_facility in cities) <= max_facilities)

    # objective function
    m.obj = Objective(sense=minimize, expr=sum(
        nx.shortest_path_length(game_graph, source=possible_facility, target=city) * m.x[possible_facility, city] for
        possible_facility in cities for city in cities))

    solver = SolverFactory('cbc')
    solver.solve(m, tee=False)

    Output = namedtuple('station_placement', 'selections objective_value')
    result = Output(tuple(city for city in cities if m.y[city] == 1),
                    m.obj())
    return result
