# Implement the data structure (class) that keeps only unique elements and uses the python list
# as a container for elements. The data structure should have following methods:
# - a method that adds an element
# - a method that returns an index of an element
# - a method that removes an element by index
# - a method that gets an another object of that data structure as a parameter, and returns a
# new object that contains symmetric difference between objects ( symm diff - is all
# elements excluding common, ie for two lists A=[1, 3, 5, 7] and B=[2, 3, 4, 7, 8] symm diff
# of their elements is [1, 2, 4, 5, 8])
# We assume that every method has a corresponding test or set of tests. Everything should be
# written in python.

class Set:
    """ Represents Set class """

    def __init__(self, iterable=[]):
        """ Initialize Set """
        self.elements = []
        for element in iterable:
            self.add(element)

    def add(self, element):
        """ Method that adds an element """
        if element not in self.elements:
            self.elements.append(element)
        else:
            self.elements[self.get_index(element)] = element

    def get_index(self, element):
        """ Method that returns an index of an element """
        return self.elements.index(element)

    def remove(self, index):
        """ Method that removes an element by index """
        del self.elements[index]

    def symmetric_difference(self, set):
        """ Symmetric difference """
        result = Set()
        for element in self:
            if element not in set:
                result.add(element)
        for element in set:
            if element not in self:
                result.add(element)
        return result

    def __eq__(self, set):
        return self.elements == set.elements

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def __next__(self):
        return next(self.elements)

    def __str__(self):
        string_representation = "["
        for element in self:
            string_representation += str(element)
            if self.get_index(element) != len(self.elements) - 1:
                string_representation += ", "
        string_representation += "]"
        return string_representation
