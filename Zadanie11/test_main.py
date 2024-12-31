import unittest
from main import SingleList, Node

class TestSingleList(unittest.TestCase):

    def setUp(self):
        self.list1 = SingleList()
        self.list2 = SingleList()
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4)
        self.node5 = Node(5)

    def test_insert_head(self):
        self.list1.insert_head(self.node1)
        self.assertEqual(self.list1.head, self.node1)
        self.assertEqual(self.list1.tail, self.node1)
        self.assertEqual(self.list1.count(), 1)

        self.list1.insert_head(self.node2)
        self.assertEqual(self.list1.head, self.node2)
        self.assertEqual(self.list1.tail, self.node1)
        self.assertEqual(self.list1.count(), 2)

    def test_insert_tail(self):
        self.list1.insert_tail(self.node1)
        self.assertEqual(self.list1.head, self.node1)
        self.assertEqual(self.list1.tail, self.node1)
        self.assertEqual(self.list1.count(), 1)

        self.list1.insert_tail(self.node2)
        self.assertEqual(self.list1.tail, self.node2)
        self.assertEqual(self.list1.count(), 2)

    def test_remove_head(self):
        self.list1.insert_tail(self.node1)
        self.list1.insert_tail(self.node2)
        removed_node = self.list1.remove_head()
        self.assertEqual(removed_node, self.node1)
        self.assertEqual(self.list1.head, self.node2)
        self.assertEqual(self.list1.count(), 1)

        self.list1.remove_head()
        self.assertTrue(self.list1.is_empty())

        with self.assertRaises(ValueError):
            self.list1.remove_head()

    def test_remove_tail(self):
        self.list1.insert_tail(self.node1)
        self.list1.insert_tail(self.node2)
        removed_node = self.list1.remove_tail()
        self.assertEqual(removed_node, self.node2)
        self.assertEqual(self.list1.tail, self.node1)
        self.assertEqual(self.list1.count(), 1)

        removed_node = self.list1.remove_tail()
        self.assertEqual(removed_node, self.node1)
        self.assertTrue(self.list1.is_empty())

        with self.assertRaises(ValueError):
            self.list1.remove_tail()

    def test_join(self):
        self.list1.insert_tail(self.node1)
        self.list1.insert_tail(self.node2)
        self.list2.insert_tail(self.node3)
        self.list2.insert_tail(self.node4)

        self.list1.join(self.list2)
        self.assertEqual(self.list1.count(), 4)
        self.assertEqual(self.list1.tail, self.node4)
        self.assertTrue(self.list2.is_empty())

    def test_clear(self):
        self.list1.insert_tail(self.node1)
        self.list1.insert_tail(self.node2)
        self.list1.clear()
        self.assertTrue(self.list1.is_empty())
        self.assertEqual(self.list1.count(), 0)

if __name__ == '__main__':
    unittest.main()
