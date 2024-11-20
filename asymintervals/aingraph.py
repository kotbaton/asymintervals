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

        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        for i, a in zip(self.graph.nodes, self.list_of_ains):
            # self.graph.nodes[i]['label'] = f'$[{a.lower}, {a.upper}]_{{{a.expected}}}$'
            self.graph.nodes[i]['label'] = chr(ord('A') + i)
            self.graph.nodes[i]['color'] = colors[i % len(colors)]

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
        node_color = nx.get_node_attributes(self.graph, 'color')
        # Ensure correct order even if graph changed
        node_color = [node_color[i] for i in range(len(node_color))]
        nx.draw_networkx_nodes(G=self.graph,
                               node_size=1000,
                               node_color=node_color,
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

    def plot_intervals(self, ax: plt.Axes = None):
        """
        Visualizes the intervals of the AIN objects in a horizontal stacked manner, organized by levels to avoid overlap.

        Parameters
        ----------
        ax : plt.Axes, optional
            The Matplotlib axis to draw the intervals on. If None, the current axis (`plt.gca()`) will be used.

        Returns
        -------
        matplotlib.axes.Axes
            The axis on which the intervals are plotted.

        Notes
        -----
        - Intervals are grouped into levels to avoid overlap in the visualization. Each level contains intervals
          that do not overlap or touch each other.
        - Each interval is displayed as a horizontal line with markers for its lower bound, expected value, and upper bound.
        - Labels corresponding to the interval indices are displayed next to the intervals.
        """
        if ax is None:
            ax = plt.gca()

        levels = []
        added_ains = set()
        for i, a in enumerate(self.list_of_ains):
            # Create a new level and add single AIN here if not already added
            if i in added_ains:
                continue

            levels.append([i])
            added_ains.add(i)

            # Add to this level any other AIN which not overlaps and is not already added
            for j, b in enumerate(self.list_of_ains):
                if j in added_ains:
                    continue

                if (a > b) * (a < b) != 0 or (a.lower == b.upper) or (a.upper == b.lower):
                    continue

                levels[-1].append(j)
                added_ains.add(j)

        for i, level in enumerate(levels):
            for ain_idx in level:
                ain = self.list_of_ains[ain_idx]
                ax.plot([ain.lower, ain.expected, ain.upper], [i] * 3,
                        marker='$|$',
                        markersize=10,
                        color=self.graph.nodes[ain_idx]['color'],
                        linewidth=2)
                ax.text(ain.lower, i, f'{chr(ord('A') + ain_idx)} ',
                        ha='right', va='center', fontsize=12)

        ax.set_yticks([])
        ax.set_ylim(-0.5, len(levels) - 0.5)

        return ax