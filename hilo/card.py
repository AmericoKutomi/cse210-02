import random

class Card:
    """A flat piece of paper or plastic that has a value from 1 to 13 (and a suit) 
        on one side, and on the other side, has a face that prevents its identification.

    The responsibility of a Card is to hold and show one value in the range of 1 to 13.
   
    Attributes:
        value (int): The value expressed by a number in one of the sides.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def get_value(self):
        """Generates a new random value for the card
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 6)

