# Search methods

import search

ab = search.GPSProblem('A', 'U'
                       , search.romania)

print("breadth:")
print(search.breadth_first_graph_search(ab).path())
print("depth:")
print(search.depth_first_graph_search(ab).path())
print("acot: ")
print(search.ram_acot_graph_search(ab).path())
print("acot with subestimation: ")
print(search.ram_acotSub_graph_search(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
