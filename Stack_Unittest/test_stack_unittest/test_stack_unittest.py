import unittest

from stack import Node, Stack


class TestNode(unittest.TestCase):
    # test_node = Node('test_data')

    def test_01_node_init(self):
        test_node = Node('test_data')
        self.assertEqual(test_node.data, 'test_data')
        self.assertEqual(test_node.next_node, None)
        test_node_2 = Node('test_data_2', test_node)
        self.assertEqual(test_node_2.data, 'test_data_2')
        self.assertEqual(test_node_2.next_node, test_node)
        self.assertEqual(test_node_2.next_node.data, 'test_data')


class TestStack(unittest.TestCase):
    test_stack = Stack(2)

    def test_02_stack_init(self):
        self.assertEqual(TestStack.test_stack.stack_size, 2)
        self.assertEqual(TestStack.test_stack.top, None)

    def test_03_push(self):
        self.assertEqual(TestStack.test_stack.push(10.5), None)
        self.assertEqual(TestStack.test_stack.push(11), None)
        self.assertEqual(TestStack.test_stack.push(12), 'Стек переполнен')

    def test_04_get_data(self):
        self.assertEqual(TestStack.test_stack.get_data(0), 11)

    def test_05_is_full(self):
        self.assertEqual(TestStack.test_stack.is_full(), True)

    def test_06_size_stack(self):
        self.assertEqual(TestStack.test_stack.size_stack(), 2)

    def test_07_counter_int(self):
        self.assertEqual(TestStack.test_stack.counter_int(), 1)

    def test_08_pop(self):
        self.assertEqual(TestStack.test_stack.pop(), 11)
        self.assertEqual(TestStack.test_stack.pop(), 10.5)
        self.assertEqual(TestStack.test_stack.pop(), 'Стек пуст')

    def test_09_is_full(self):
        self.assertEqual(TestStack.test_stack.is_full(), False)

    def test_10_is_empty(self):
        self.assertEqual(TestStack.test_stack.is_empty(), True)

    def test_11_clear_stack(self):
        self.assertEqual(TestStack.test_stack.clear_stack(), None)
        self.assertEqual(TestStack.test_stack.is_empty(), True)

    def test_12_get_data(self):
        self.assertEqual(TestStack.test_stack.get_data(1), 'Out of range')


