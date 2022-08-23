"""
Tree Abstract Base Class
"""


class Tree:
    """Abstract base clase representing a tree structure."""
    class Position:
        """An abstraction representing the location of a single element."""
        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError("Method must be implemented by a subclass")
        
        def __eq__(self, other: object) -> bool:
            """Return True if other represents the same location"""
            raise NotImplementedError("method must be implemented by a sublcass")
        
        def __ne__(self, other: object) -> bool:
            """Return True if other does not represent the same location"""
            return not (self == other)
