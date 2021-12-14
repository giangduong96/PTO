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
    def num_children(self, position):
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


class binarytree(Tree):
    """ abstract base class representing a binary tree structure"""
    def left(self, position):
        """ return a Position representing position's left child """
        """ return None if p does NOT have a left child"""
        raise (" Must be implemented by subclass")

    def right(self, position):
        """ return a Position representing position's right child """
        """ return None if p does NOT have a right child"""
        raise (" Must be implemented by subclass")

    def sibling(self, position):
        """ return a position representing position p sibbling or NONE if no sibling"""
        parent = self.parent(position)
        if parent is None:
            return None
        else:
            if position == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, position):
        """generate an iteration of Position representing position's children"""
        if self.left(position)is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield  self.right(position)

class LinkedBinaryTree(binarytree):
    """ Linked representation of ba binary tree structure """
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent = None, left =None, right =None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(Tree.Position):
        """ an abstract representing the location of a single element """
        def __init__(self, container, node):
            """constructor should not be invoked by user """
            self._container = container
            self._node = node

        def element(self):
            """return the element stored at his Position """
            return self._node._element

        def __eq__(self, other):
            """ return True if other is a position representing the same location """
            return type(other) is type(self) and other._node is self._node

    def _validate(self, position):
        """ return associate node if position is valid """
        if not isinstance(position, self.Position):
            raise ("P must be proper Position type \n")
        if position._container is not self:
            raise (" P is not belong to this container")
        if position._node._parent is position._node:
            # convention for deprecated container
            raise ValueError("P is no longer valid")
        return position._node

    def _make_position(self, node):
        """ return position instance for given node (or None if no node"""
        return self.Position(self, node) if node is not None else None

    # Binary tree constructor

    def __init__(self):
        """create an initially empty binary tree """
        self._root = None
        self._size = 0
    # Public accessors

    def __len__(self):
        """ return the root position of the tree or None if tree is empty """
        return self._size

    def root(self):
        """ return the root position of of the tree"""
        return  self._make_position(self._root)

    def parent(self,position):
        """ return the Position of parent Or None if P is root"""
        node = self._validate(position)
        return self._make_position(node._parent)

    def left(self,position):
        """ return the position of left node Or None if P has no a left child"""
        node = self._validate(position)
        return self._make_position(node._left)

    def right(self, position):
        """ return the position of right node or None if P has no right child"""
        node = self._validate(position)
        return self._make_position(node._right)

    def num_children(self, position):
        """ return the number of children of the Position P"""
        node = self._validate(position)
        count = 0
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
        return count

    def _add_root(self, element):
        """ place element at the root of an empty tree and return new Position
        Raise value of tree is nonempty
        """
        if self._root is not None: raise ValueError("Root exist!\n")
        self._size  =1
        self._root= self._Node(element)
        return self._make_position(self._root)

    def _add_left(self,position, element):
        """
        create a new left child for Position P, store element e
        Return the position of new node
        Raise valueErrro if Postion P is invalid or already have left child
        """
        node = self._validate(position)
        if node._left is not None: raise ValueError("Left Child exists\n")
        self._size +=1
        node._left = self._Node(element, node)
        return self._make_position(node._left)

    def _add_right(self, position, element):
        """ create a new right child for Position P and store element e
        Return the position of new node
        raise ValueError if position P is invalid or already have right child"""
        node = self._validate(position)
        if node._right is not None: raise ValueError("Right child exists\n")
        self._size += 1
        node._left = self._Node(element, node)
        return self._make_position(node._right)

    def _replace(self, position, element):
        """ replace the element at position p with element and return old element """
        node = self._validate(position)
        old = node._element
        node._element = element
        return old

    def _delete(self, position):
        """ Delete the node at Position P and replace it with its chold if any
        return the element that had been store at Position p
        Raise ValueError if Position P is invalid or P has 2 children
        """
        node = self._validate(position)

        if self.num_children(position) == 2: raise ValueError("P has 2 children")
        child = node._left if node._left else node._right       # maybe None

        if child is not None:
            child._parent = node._parent        # child's grandparent becomes parent

        if node is self._root:
            self._root = child                  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                     # convention for deprecated node
        return node._element


    def _attach(self, position, t1, t2):
        """" Attach trees t1 and t2 as left and right subtrees of external p """
        node = self._validate(position)
        if not self.is_leaf(position): raise ValueError(" Position must be leaf\n")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must be matched \n")
        self._size += len(t1) +len(t2)

        if not t1.is_emtpy():               # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None                 # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():               # attach t1 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None                 # set t2 instance to empty
            t2._size = 0









