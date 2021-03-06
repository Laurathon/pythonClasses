"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """ initializing object, starting at number """
        self.start = start

    def __repr__(self):
        return f"<Serial starts at {self.start} returns {self.generate()}>"              

    def generate(self):
        self.start +=1
        return self.start -1

    def reset(self):
        self.start =100
        
