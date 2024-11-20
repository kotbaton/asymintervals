from itertools import combinations

import matplotlib.pyplot as plt
import networkx as nx

from .asymintervals import AIN


class AINGraph:
    """
    Represents a graph of AIN (Asymmetric Interval Number) objects. Each node corresponds to an AIN object,
    and edges are weighted relationships based on their interval overlap.

    Attributes
    ----------
    list_of_ains : list[AIN] or tuple[AIN]
        A list or tuple of AIN objects that form the nodes of the graph.
    graph : nx.Graph
        A NetworkX graph representing the relationships between the AIN objects.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from asymintervals import AIN, AINGraph
    >>> g = AINGraph([
    ...      AIN(0, 2),
    ...      AIN(1, 5),
    ...      AIN(3, 4)
    ... ])
    >>> g.plot_graph()
    >>> # plt.show() # Uncomment to show the graph
    """
    def __init__(self, list_of_ains: list[AIN] | tuple[AIN]):
        """
        Initializes the AINGraph with a list or tuple of AIN objects and constructs an undirected weighted graph.

        Parameters
        ----------
        list_of_ains : list[AIN] or tuple[AIN]
            A list or tuple containing AIN objects.

        Raises
        ------
        ValueError
            If any element in `list_of_ains` is not an instance of the AIN class.
        """
        if not all(isinstance(ain, AIN) for ain in list_of_ains):
            raise ValueError('`list_of_ains` argument should be a list or tuple of AIN objects.')

        self.list_of_ains = list_of_ains
        self.graph = nx.Graph()
        for (i, a), (j, b) in combinations(enumerate(list_of_ains, 0), 2):
            w = (a > b) * (a < b)
            if w > 0:
                self.graph.add_edge(i, j, weight=w)

        for i, a in zip(self.graph.nodes, self.list_of_ains):
            self.graph.nodes[i]['label'] = f'$[{a.lower}, {a.upper}]_{{{a.expected}}}$'

    def __repr__(self):
        """
        Returns a concise string representation of the AINGraph instance.

        Returns
        -------
        str
            A string containing the class name and the list of AIN objects.
        """
        return f'{self.__class__.__name__}({self.list_of_ains})'

    def __str__(self):
        """
        Returns a detailed string representation of the AINGraph instance, including nodes and edges.

        Returns
        -------
        str
            A detailed string describing the graph structure.
        """
        edges = '\n'.join(f'\t{self.list_of_ains[i]} --- {self.graph.edges[i, j]['weight']:^0.6f} --- {self.list_of_ains[j]}'
                          for i, j in self.graph.edges)
        return f'{self.__class__.__name__} with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges.\n' \
               f'Nodes:\n\t{"\n\t".join(str(self.list_of_ains[i]) for i in self.graph.nodes)}\n'\
               f'Edges:\n{edges}'

    def add_ain(self, new_ain):
        """
        Adds a new AIN object to the graph and updates the graph structure.

        Parameters
        ----------
        new_ain : AIN
            The AIN object to add to the graph.
        """
        raise NotImplementedError('Not implemented yet.')

    def plot_graph(self, precision: int = 4, ax: plt.Axes = None):
        """
        Visualizes the graph using Matplotlib. Displays nodes, edges, and weights.

        Parameters
        ----------
        precision : int, optional
            Number of decimal places for edge weight labels. Defaults to 4.
        ax : matplotlib.axes.Axes, optional
            The Matplotlib axis to draw the graph on. If None, a new axis is created.

        Returns
        -------
        plt.Axes
            Axes object on which the graph was drawn.
        """
        if ax is None:
            ax = plt.gca()

        # Get positions for all nodes
        pos = nx.circular_layout(self.graph)

        # Draw nodes
        nx.draw_networkx_nodes(G=self.graph,
                               node_size=2500,
                               node_color='tab:orange',
                               linewidths=2,
                               edgecolors='k',
                               pos=pos,
                               ax=ax)

        # Draw node labels
        node_labels = nx.get_node_attributes(self.graph, 'label')
        nx.draw_networkx_labels(G=self.graph,
                                labels=node_labels,
                                pos=pos,
                                ax=ax)

        # Draw edges
        nx.draw_networkx_edges(G=self.graph,
                               width=2,
                               pos=pos,
                               ax=ax)

        # Draw edge weights (labels)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        edge_labels = {e: f'{w:0.{precision}f}' for e, w in edge_labels.items()}
        nx.draw_networkx_edge_labels(G=self.graph,
                                     edge_labels=edge_labels,
                                     pos=pos,
                                     ax=ax)

        ax.margins(0.1)
        ax.axis('off')
        return ax
