from typing import Optional

from Types.__graph_node__ import Node


class Solution:
    def cloneGraph(self, node: 'Node') -> Optional[Node]:
        if not node:
            return None
        visited = {node: Node(node.val)}

        def traverse(current):
            nonlocal visited
            for n in current.children:
                if n not in visited:
                    new_node = Node(n.val)
                    visited[n] = new_node
                    traverse(n)
                visited[current].children.append(visited[n])

        traverse(node)
        return visited[node]
