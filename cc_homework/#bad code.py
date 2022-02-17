#bad code
class TreeNode: #defies a node in the tree, data, parent, child

    def __init__(self,data):
        self.data = data
        self.chld = []
        self.prnt = None
    def add_child(self, child ):
        child.prnt = self
        self.chld.append(child)
        return child
    def get_level(self):
        level = 0
        p = self.prnt
        while p:
            level += 1
            p = p.prnt
        return level
    def prnt_t(self):
        spaces = '   ' * self.get_level()
        prefix = spaces + "|__" if self.prnt else ""
        print(prefix + self.data)
        if self.chld:
            for child in self.chld:
                child.prnt_t()

#      def prnt_t(self):
#        spaces = '   ' * self.get_level()
#        prefix = spaces + "|__" if self.prnt else ""
#        print(prefix + self.data)
#        if self.chld:
#            for child in self.chld:
#                child.prnt_t()



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


root.prnt_t()


###############################################################
#using shorter words like prnt for print and chld for child doesnt make it easier for the code to be interpreted
#line 32-38 is an example of bad code due to the duplication of code
#in line 24 it is def prnt_t for print tree but tree is denoted as t which makes it harder to understand
#no comments to make it more easier to understand
#the absent of spaces between each def and line can cause the code to look claustrophobic and messy