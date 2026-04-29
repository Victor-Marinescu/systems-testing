import unittest
from tree import Tree

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        """ Cream un arbore de testare"""
        self.tree = Tree()
        # adugam valori
        for val in [5, 3, 7, 2, 4]:
            self.tree.add(val)

    def test_find_existing_element(self):
        """ Testam daca gaseste un element in arbore """
        node = self.tree.find(3)
        self.assertIsNotNone(node, "Nodul ar fi trebuit sa fie gasit.")
        self.assertEqual(node.data, 3, "Datele din nodul gasit nu corespund.")

    def test_find_non_existing_element(self):
        """ Testam comportamentul pentru un element care nu exista """
        node = self.tree.find(99)
        self.assertIsNone(node, "Nodul nu ar fi trebuit să fie găsit (valoare inexistentă).")

    def test_find_in_empty_tree(self):
        """ Testam cautarea intr-un arbore gol """
        empty_tree = Tree()
        self.assertIsNone(empty_tree.find(5), "Cautarea intr-un arbore gol trebuie sa returneze None.")

if __name__ == '__main__':
    unittest.main()