import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from levels import Node, level_order, zigzag_level_order, right_side_view

def demo():
    #       4
    #     2   6
    #    1 3 5 7
    return Node(4,
                Node(2, Node(1), Node(3)),
                Node(6, Node(5), Node(7)))

# normal (4)
def test_levels_basic():
    r = demo()
    assert level_order(r) == [[4],[2,6],[1,3,5,7]]

def test_zigzag_basic():
    r = demo()
    assert zigzag_level_order(r) == [[4],[6,2],[1,3,5,7]]

def test_right_view_basic():
    r = demo()
    assert right_side_view(r) == [4,6,7]

def test_single_node():
    r = Node(1)
    assert level_order(r) == [[1]]
    assert zigzag_level_order(r) == [[1]]
    assert right_side_view(r) == [1]

# edge (3)
def test_empty_tree():
    assert level_order(None) == []
    assert zigzag_level_order(None) == []
    assert right_side_view(None) == []

def test_left_chain():
    r = Node(1, Node(2, Node(3)))
    assert right_side_view(r) == [1,2,3]

def test_right_chain():
    r = Node(1, None, Node(2, None, Node(3)))
    assert level_order(r) == [[1],[2],[3]]

# harder (3)
def test_unbalanced():
    r = Node(1, Node(2, None, Node(4)), Node(3))
    assert zigzag_level_order(r) == [[1],[3,2],[4]]

def test_wide_level():
    r = Node(0)
    r.left = Node(1, Node(3), Node(4))
    r.right = Node(2, Node(5), Node(6))
    assert right_side_view(r) == [0,2,6]

def test_random_shape_levels():
    r = Node(5, Node(1, Node(0), None), Node(9, Node(7), Node(10)))
    assert level_order(r)[0] == [5]
