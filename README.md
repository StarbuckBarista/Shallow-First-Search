# Shallow-First-Search
A fun path-finding algorithm that bests Depth First Search.

Current Version: `0.1.0`

## Installation

TODO

## Getting Started

First, visualize a Directed or Undirected Graph that you would like to draw. For the sake of this example, I will draw an Undirected Graph with four nodes.

![Undirected Graph](https://i.ibb.co/3RQyTs1/shallow-First-Image1.png)

```Python
import shallow_first_search as sfs

undirectedGraph = sfs.Diagraph()

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

For more detailed documentation and available options, visit https://whatever

## Examples

Various examples on how to use Shallow-First-Search can be found in the [examples folder](https://whatever).
