from enum import Enum

class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"

class CardType(Enum):
    NUMBER = "number"
    SKIP = "skip"
    REVERSE = "reverse"
    DRAW_TWO = "draw_two"
    WILD = "wild"
    DRAW_FOUR = "draw_four"

class Card:
    def __init__(self, card_type, color = None, number = None):
        self.card_type = card_type
        self.color = color
        self.number = number

    def is_number(self):
        return self.card_type == CardType.NUMBER

    def is_wild(self):
        return self.card_type == CardType.WILD or self.card_type == CardType.DRAW_FOUR
    
    def points(self):
        if self.is_number():
            return self.number
        elif self.is_wild():
            return 50
        else:
            return 20

    def __str__(self):
        if self.is_number():
            return f"{self.color.value} {self.number}"
        elif self.is_wild():
            return self.card_type.value.replace('_', ' ')
        else:
            return f"{self.color.value} {self.card_type.value.replace('_', ' ')}"
        