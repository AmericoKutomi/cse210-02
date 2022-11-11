from card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (Card): The first card.
        next_card (Card): The second card, used to be compared with the first card.
        guess (string): The choice made by the player by guessing the relation between the first and the next card.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.next_card = Card()
        self.guess = ''
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.show_card()
            self.get_input()
            self.show_next_card()
            self.make_evaluation()
            self.show_score()

    def show_card(self):
        """Displays the first card.
        Args:
            self (Director): An instance of Director.
        """
        self.card.get_value()
        print(f"\nThe card is: {self.card.value}")

    def get_input(self):
        """Ask the user if the next card is Higher or Lower than the first card

        Args:
            self (Director): An instance of Director.
        """
        self.guess = input("Higher or lower? [h/l] ")

    def show_next_card(self):
        """Displays the first card.
        Args:
            self (Director): An instance of Director.
        """
        self.next_card.get_value()
        print(f"Next card is: {self.next_card.value}")

    def make_evaluation(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if self.guess == 'h':
            if self.next_card.value > self.card.value:
                self.score = 100
            else:
                self.score = -75
        else:
            if self.next_card.value < self.card.value:
                self.score = 100
            else:
                self.score = -75

        self.total_score += self.score

    def show_score(self):
        """Displays the score. 
            If the score is negative or zero, it stops the game. 
            If the score is positive, asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.total_score}\n")

        if self.total_score <= 0:
            self.is_playing = False
            print('Game over.')
        else:
            option = input("Play again? [y/n] ")
            if option == 'n':
                self.is_playing = False
