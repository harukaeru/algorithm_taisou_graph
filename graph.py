from collections import defaultdict
import graphviz
import rep

g = defaultdict(list)
for i in range(1, len(rep.y)):
    a = rep.y[i - 1]
    a = rep.rev_conv[a]

    b = rep.y[i]
    b = rep.rev_conv[b]

    g[a].append((b, i))

from pprint import pprint
print('graph-----------------')
pprint(g)
dot = graphviz.Digraph(format='png')
for l_node, r_nodes in g.items():
    for r_node, order in r_nodes:
        dot.edge(l_node, r_node, label=str(order))
dot.graph_attr['dir'] = 'LR'
dot.edge_attr.update(arrowhead='vee')

print(dot.source)

print('--------------------')
dot.render()
