from altgraph import Graph, Dot

# create a graph
edges = [ (1,2), (1,3), (3,4), (3,5), (4,5), (5,4) ]
graph = Graph.Graph(edges)

# create a dot representation of the graph
dot = Dot.Dot(graph)

# display the graph
dot.display()

# save the dot representation into the mydot.dot file
dot.save_dot(file_name='mydot.dot')

# save dot file as gif image into the graph.gif file
dot.save_img(file_name='graph', file_type='gif')