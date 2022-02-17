#good code
class TreeNode: #defies a node in the tree, data, parent, child

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child ):
        child.parent = self
        self.children.append(child)
        return child

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self):
        spaces = '   ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

root = TreeNode('Electronics')
laptops = TreeNode('Laptops')
root.add_child(laptops)
laptops.add_child(TreeNode('Dell'))
laptops.add_child(TreeNode('Macbook'))
laptops.add_child(TreeNode('Acer'))

phones = TreeNode ('Phones')
root.add_child(phones)
phones.add_child(TreeNode('iPhone'))
phones.add_child(TreeNode('Samsung'))

accessories = TreeNode('Accessories')
root.add_child(accessories)
accessories.add_child(TreeNode('Galaxy Cover'))
accessories.add_child(TreeNode('KeyChain'))


root.print_tree()
