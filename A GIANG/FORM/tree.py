class Tree:
    """
    abstract base class representing a tree structure
    """
    class Position:
        """
        Nested class - an abstract representing the location of a single element
        """
        def element(self):
            """ return the element stored at this Position """
            raise (" Must be implemented by subclass")
        def __eq__(self, other):
            """ return True if other position represents the same location"""
            raise (" Must be implemented by subclass")
        def __ne__(self, other):
            """ return True if other position represents not the same location"""
            return not (self == other)
    def root(self):
        """ return position representing the tree's root or None if empty """
        raise (" Must be implemented by subclass")
    def parent(self,position):
        """return Position representing parents node or NONE if P is root"""
        raise (" Must be implemented by subclass")
    def num_children(self, parent):
        """ return the number of children that Position P has"""
        raise (" Must be implemented by subclass")
    def children(self, parent):
        """ genarate an iteration of Position representing parent children """
        raise (" Must be implemented by subclass")
    def __len__(self):
        """ Return total number of element in the tree """
        raise (" Must be implemented by subclass")
    def is_root(self, position):
        """ return True if Position P representing the root of the tree """
        return self.root() == position
    def is_leaf(self, position):
        """ return True if Position P does NOT have any children"""
        return self.num_children(position) == 0
    def is_empty(self):
        """ return True if the tree is empty"""
        return self.__len__() == 0
    def depth(self, position):
        """ depth is different to height
        depth count from the root: depth at root  == 0
        return the number of levels separating Position p from the root"""
        if self.is_root(position):
            return 0
        else:
            return 1 + self.depth(self.parent(position))
    def _height(self, position):
        """ height is count from the leaf. p is a leaf then the height of p == 0
        return the height of the subtree rooted at Position P"""
        if self.is_leaf(position):
            return  0
        else:
            return 1 + max(self._height(c) for c in self.children(position))
