# Shallow-First-Search
A fun path-finding algorithm that bests Depth First Search.

Current Version: `0.1.0`

## Installation

Launch your Command Prompt and type in the command `git clone https://github.com/StarbuckBarista/Shallow-First-Search`. This will create a copy of the code in this repository. Next, find the cloned file and extract the `shallow_first_search` directory from it. Finally, drag this directory into your code project's directory and you are good to go.

## Getting Started

First, visualize a Directed or Undirected Graph that you would like to draw. For the sake of this example, I will draw an Undirected Graph with four nodes.

![Undirected Graph](https://i.ibb.co/3RQyTs1/shallow-First-Image1.png)

```Python
import shallow_first_search.main as sfs

undirectedGraph = sfs.Graph()

nodeA = sfs.Node("A")
nodeB = sfs.Node("B")
nodeC = sfs.Node("C")
nodeD = sfs.Node("D")
edgeAB = sfs.Edge(nodeA, nodeB)
edgeBC = sfs.Edge(nodeB, nodeC)
edgeCD = sfs.Edge(nodeC, nodeD)

undirectedGraph.addEdge(edgeAB)
undirectedGraph.addEdge(edgeBC)
undirectedGraph.addEdge(edgeCD)

path = shortestPath(g, g.getNode("A"), g.getNode("D"))
print(sfs.evaluateAnswer(path))
```

For more detailed documentation and available options, visit https://github.com/StarbuckBarista/Shallow-First-Search/wiki/Documentation

## Examples

Various examples on how to use Shallow-First-Search can be found in the [examples folder](https://github.com/StarbuckBarista/Shallow-First-Search/tree/main/examples).
