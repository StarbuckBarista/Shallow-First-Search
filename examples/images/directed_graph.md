# Example: Directed Graph

First, visualize a Directed Graph that you would like to draw. For the sake of this example, I will draw an a graph with four nodes.

![Undirected Graph](https://i.ibb.co/r3p1h5R/shallow-First-Image2.png)

```Python
import shallow_first_search.main as sfs

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
