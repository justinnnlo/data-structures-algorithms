# dfs uses a stack
# Stack is visualized as a vertical structure and hence has depth - DFS.
# deep -> explore a branch -> go as deep as we can -> then explore another branch and repeat

# whenever we are at a given node aka for each node -> we are adding that node's name to the final array -> for every child node we are going to call the dfs function and pass in the final array

# Time complexity : O(V + E)
# Space complexity : O(V) stack frame (in case worst case of a one sided tree that keeps calling dfs) + the dfs final array we storing


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
