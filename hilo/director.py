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
        # card and next_card are instances of the class Card
        self.card = Card()
        self.next_card = Card()

        # these states are to control the flow of the game
        self.guess = ''
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # the loop controls the flow of the game and it stops and is_playing is set to False
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
        # the get_value method of class Card is called to assign an integer value to the card
        self.card.get_value()
        print(f"\nThe card is: {self.card.value}")

    def get_input(self):
        """Ask the user if the next card is Higher or Lower than the first card

        Args:
            self (Director): An instance of Director.
        """
        # Ask the user guess
        self.guess = ''
        while self.guess != 'h' and self.guess != 'l':
            self.guess = input("Higher or lower? [h/l] ").lower()

    def show_next_card(self):
        """Displays the first card.
        Args:
            self (Director): An instance of Director.
        """
        # the get_value method of class Card is called to assign an integer value this time to the second card
        self.next_card.get_value()
        print(f"Next card is: {self.next_card.value}")

    def make_evaluation(self):
        """ Compares the values of the two cards.
            The player's score is obtained according to his guess and the card values.

        Args:
            self (Director): An instance of Director.
        """

        if self.guess == 'h':                               # the user guessed higher
            if self.next_card.value > self.card.value:      # the second card is higher than the first
                self.score = 100
            else:
                self.score = -75                            # the score can be positive or negative

        else:                                               # the user guessed lower
            if self.next_card.value < self.card.value:      # the second card is lower than the first
                self.score = 100
            else:
                self.score = -75

        self.total_score += self.score                      # the round score is added to the overall score

    def show_score(self):
        """ Displays the score and decides the next step.
            If the score is negative or zero, it stops the game. 
            If the score is positive, asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.total_score}\n")

        if self.total_score <= 0:                           # a zero or a negative total score will end the game
            self.is_playing = False                         # when is_playing is set to False, it will cause the game to stop in the next loop
            print('Your score is not enough to continue.')
            print('Game over.')
        else:
            option = ''
            while option != 'y' and option != 'n':
                option = input("Play again? [y/n] ").lower()  # the player has the option to continue or not

                if option != 'y' and option != 'n':         # if the option is not valid, continue statement return to the loop
                    continue

                if option == 'n':
                    self.is_playing = False
                    print('Thanks for playing.')
                    print('Game over.')


