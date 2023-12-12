import networkx as nx
import matplotlib.pyplot as plt


def add_edge_to_graph(G, e1, e2, w):
    G.add_edge(e1, e2, weight=w)

def create_plot(points, edges):
    # create graph
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(points)

    # you want your own layout
    # pos = nx.spring_layout(G)
    pos = {point: point for point in points}

    # add axis
    fig, ax = plt.subplots()
    # nx.draw(G, pos=pos, node_color='k', ax=ax)
    nx.draw(G, pos=pos, node_size=70, ax=ax)  # draw nodes and edges
    # nx.draw_networkx_labels(G, pos=pos)  # draw node labels/names
    # nx.draw_networkx_edge_labels(G, pos, ax=ax)
    plt.axis("on")
    ax.set_xlim(0, 11)
    ax.set_ylim(0,11)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.savefig("graph.png")  # save as png
    plt.show()