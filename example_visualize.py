# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def main():
    # Build a dataframe with your connections
    df = pd.DataFrame({'from': ['A', 'B', 'C', 'A'], 'to': ['D', 'A', 'E', 'C']})
    print(df)

    # Build your graph
    G = nx.from_pandas_dataframe(df, 'from', 'to')

    # Graph with Custom nodes:
    nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=40)
    plt.show()


if __name__ == '__main__':
    main()
