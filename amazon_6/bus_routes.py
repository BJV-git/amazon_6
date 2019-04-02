
import collections
def busroutesmiin(routes, S, T):
    to_routes= collections.defaultdict(set)
    for i, route in enumerate(routes):
        for j in route: to_routes[j].add(i) # for each routes what are the buseses

    bfs=[(S,0)]
    seen = set([S])

    for stop, bus in bfs:
        if stop == T: return bus
        for route_i in to_routes[stop]: # for each bus at that stop
            for next in routes[route_i]: # for all stops for that bus
                if next not in seen:
                    bfs.append((next, bus+1))
                    seen.add(next)
            routes[route_i] = []

    return -1