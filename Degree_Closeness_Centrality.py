import csv
import random
import copy
import networkx as nx

#Code takes in the network in column format. Network must have the following headers [Source] [Target] [Association]
#The code then calculates the degree for each node and closeness centrality. It will output 4 files,
# the calculation for the original network, for 10% of edges removed for 20% of edges removed and 30% of edges removed.


# Inputs ================================================================================================
working_dir = r"C:\Users\rojaschavez\Desktop\Network_analysis\\"
network = "Column_fisher_baseline.csv"
output_file = 'centrality_measures_original.csv'

# Read the CSV file and create a networkx graph
graph = nx.Graph()
with open(working_dir + network) as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        source = int(row[0])
        target = int(row[1])
        association = float(row[2])
        graph.add_edge(source, target, weight=association)

# Calculate Degree centrality
degree = dict(graph.degree())

# Calculate Closeness centrality
closeness_centrality = nx.closeness_centrality(graph)

# Write the original centrality measures to a CSV file
with open(working_dir + output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Node', 'Degree', 'Closeness Centrality'])
    for node in graph.nodes():
        degree_value = degree[node]
        closeness = closeness_centrality[node]
        writer.writerow([node, degree_value, closeness])

print(f"Original centrality measures have been written to {output_file}.")

# Define the percentages of nodes to remove
percentages = [0.1, 0.2, 0.3]

# Remove nodes and calculate centrality measures for modified networks
for percentage in percentages:
    modified_graph = copy.deepcopy(graph)  # Create a copy of the original graph

    # Calculate the number of nodes to remove based on the specified percentage
    num_nodes_to_remove = int(len(modified_graph.nodes()) * percentage)

    # Randomly select and remove nodes
    nodes_to_remove = random.sample(modified_graph.nodes(), num_nodes_to_remove)
    modified_graph.remove_nodes_from(nodes_to_remove)

    # Calculate Degree centrality for the modified network
    modified_degree = dict(modified_graph.degree())

    # Calculate Closeness centrality for the modified network
    modified_closeness_centrality = nx.closeness_centrality(modified_graph)

    # Generate the output filename based on the percentage of nodes removed
    output_file_modified = f'centrality_measures_{int(percentage * 100)}_percent_removed.csv'

    # Write the modified centrality measures to a CSV file
    with open(working_dir + output_file_modified, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Node', 'Degree', 'Closeness Centrality'])
        for node in modified_graph.nodes():
            degree_value = modified_degree[node]
            closeness = modified_closeness_centrality[node]
            writer.writerow([node, degree_value, closeness])

    print(f"Centrality measures for the network with {int(percentage * 100)}% of nodes removed have been "
          f"written to {output_file_modified}.")
