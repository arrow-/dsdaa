#!/bin/env/python2

class MyStackException(Exception):
    MSG_MAP = { 0: "Stack Overflow ;P",
                1: "Stack Empty"}
    
    """Handles the Exceptions related to ``MyStack``
    
    Attributes:
        msg (str): Depending on the cause, ``Stack Overflow ;P`` or ``Stack Empty``
        max_size (int): The ``Max-Container-Size`` that has been set for ``this`` instance.
        current_size (int): The # of elements in ``this`` instance
    """
    def __init__(self, mode, max_size, current_size):
        self.msg = MyStackException.MSG_MAP[mode]
        self.max_size = full_size
        self.current_size = current_size

    def __repr__(self):
        return "MyStackException: %s CurrentSize: %d MaxSize: %d" % (self.msg, self.current_size, self.max_size)


class MyStack():
    """A standard Stack Object.
    
    The flexible ``list`` container is used to store objects. You can try *managing explicitly*, the size of the container.
    It does not have explicit memory management and relies on ``python``'s Memory Manager and garbage collection.
    
    Attributes:
        size
    
    Note:
        All methods that affect the container size throw REAL python exceptions. Use a ``try ... except`` block like this::
            
            flipStack = MyStack(7)
            try:
                flipStack.pop()
            except MyStackException as e:
                print e
                print e.msg, e.max_size, e.current_size
    
    Warning:
        Add more *"goals"* for students here??
    """
    def __init__(self, MAX_SIZE):
        """All items in the container are initialised to ``None``
        
        Args:
            MAX_SIZE (int): size of the container
        """
        self.max_stack_size = MAX_SIZE
        self.strict = strict
        # this is the stack container called '_stack'
        self._stack = [None] * self.max_stack_size
        # t is the "index" of "top-element"
        self._t = -1

    def push(self, value):
        """"pushes" ``value`` into the Stack.
        
        Arguments:
            value (object): The item to be *"pushed"*.
        
        Returns:
            bool: ``True`` if successful
        
        Raises:
            MyStackException: if the instance is full *(and overflows due to this operation)*
        """
        if (self.size() == self.max_stack_size):
            raise MyStackException(0, self.size(), self.max_stack_size)
            return False
        self._t = self._t + 1
        self._stack[self._t] = value
        return True

    def pop(self):
        """"pops" the *top* element of the instance. The instance ``size`` decreases by one *(if operation is successful)*..
        
        Returns:
            object: *top* element *if successful*
        
        Raises:
            MyStackException: if the instance is empty.
        """
        if (self.isEmpty()):
            raise MyStackException(1, self.size(), self.max_stack_size)
            return None
        temp = self._stack[self._t]
        self._stack[self._t] = None
        self._t -=1
        return temp

    def top(self):
        """
        Does not change the no. of elements in the instance.
        
        Returns:
            object: *top* element *if successful*
        
        Raises:
            MyStackException: if the instance is empty.
        """
        if (self.isEmpty()):
            raise MyStackException(1, self.size(), self.max_stack_size)
            return None
        return self._stack[self._t]        
 
    def isEmpty(self):
        """
        Returns:
            bool: ``True`` if instance is empty (no elements).
        """
        return self._t<0

    def size(self):
        return self._t+1

    def __repr__(self):
        """
        Returns a string representation of the *Stack Container*.
        If *element objects* can be represented as strings (``__repr__`` is defined for them), they will also be printed nicely!
        """
        return str(self._stack)

if __name__ == '__main__':
    ms = MyStack(1)
    print ms
    for i in range(17):
        ms.push(i**2)
        print ms