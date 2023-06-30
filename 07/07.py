#I declare the tree where I append every path and file
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def print_tree(self, level=0):
        indent = "  " * level
        print(indent + self.data)
        for child in self.children:
            child.print_tree(level + 1)     

#I declare immediately the principal directory
root = TreeNode("/");

#Variable to keep track of current directory
currentDirectory = "/"

file_path = r"C:\Users\taban\OneDrive\Documents\GitHub\AdventOfCode2022\07\input.txt"

with open(file_path, "r") as file:
    for line in file:
        if "/" in line: 
            x="/"
        if "cd" in line and "/" not in line:
            TreeNode(x).add_child(line[-1])
            x = line[-1]
            
root.print_tree()
