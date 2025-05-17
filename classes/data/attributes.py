from typing import Self
from classes.data.utils import numcheck
from math import floor

class Attribute:
    # Initialization
    def __init__(
            self,
            strength: int = 0,
            defense: int = 0,
            intellect: int = 0,
            willpower: int = 0,
            dexterity: int = 0,
            accuracy: int = 0,
            speed: int = 0,
            luck: int = 0    
        ):
        # Check for type incongruency
        if not (
                isinstance(strength, (int, float)) \
                and isinstance(defense, (int, float)) \
                and isinstance(intellect, (int, float)) \
                and isinstance(willpower, (int, float)) \
                and isinstance(dexterity, (int, float)) \
                and isinstance(accuracy, (int, float)) \
                and isinstance(speed, (int, float)) \
                and isinstance(luck, (int, float))
            ):
            raise TypeError(f"Attribute init error: Attributes must be of type int")
        
        # Check for invalid values
        if not (
                strength >= 0 \
                and defense >= 0 \
                and intellect >= 0 \
                and willpower >= 0 \
                and dexterity >= 0 \
                and accuracy >= 0 \
                and speed >= 0 \
                and luck >= 0
            ):  
            raise ValueError(f"Attribute init error: Attributes must be non-negative")
        
        self._strength = floor(strength)
        self._defense = floor(defense)
        self._intellect = floor(intellect)
        self._willpower = floor(willpower)
        self._dexterity = floor(dexterity)
        self._accuracy = floor(accuracy)
        self._speed = floor(speed)
        self._luck = floor(luck)
    
    def __str__(self) -> str:
        return f"STR: {self.strength}\nDEF: {self.defense}\nINT: {self.intellect}\nWIL: {self.willpower}\nDEX: {self.dexterity}\nACC: {self.accuracy}\nSPD: {self.speed}\nLCK: {self.luck}"

    def __repr__(self) -> str:
        return f"Attribute(strength={self.strength}, defense={self.defense}, intellect={self.intellect}, willpower={self.willpower}, dexterity={self.dexterity}, accuracy={self.accuracy}, speed={self.speed}, luck={self.luck})"
    
    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Attribute):
            raise TypeError(f"Invalid operand type: expected Attribute, got {type(other).__name__}")

        ctype = type(self)
        new_strength = self.strength + other.strength
        new_defense = self.defense + other.defense
        new_intellect = self.intellect + other.intellect
        new_willpower = self.willpower + other.willpower
        new_dexterity = self.dexterity + other.dexterity
        new_accuracy = self.accuracy + other.accuracy
        new_speed = self.speed + other.speed
        new_luck = self.luck + other.luck
        return ctype(new_strength, new_defense, new_intellect, new_willpower, new_dexterity, new_accuracy, new_speed, new_luck)

    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, Attribute):
            raise TypeError(f"Invalid operand type: expected Attribute, got {type(other).__name__}")
        
        ctype = type(self)
        new_strength = self.strength - other.strength
        new_defense = self.defense - other.defense
        new_intellect = self.intellect - other.intellect
        new_willpower = self.willpower - other.willpower
        new_dexterity = self.dexterity - other.dexterity
        new_accuracy = self.accuracy - other.accuracy
        new_speed = self.speed - other.speed
        new_luck = self.luck - other.luck

        return ctype(new_strength, new_defense, new_intellect, new_willpower, new_dexterity, new_accuracy, new_speed, new_luck)

    def __iadd__(self, other: Self) -> Self:
        if not isinstance(other, Attribute):
            raise TypeError(f"Invalid operand type: expected Attribute, got {type(other).__name__}")
        
        self.strength = self.strength + other.strength
        self.defense += other.defense
        self.intellect += other.intellect
        self.willpower += other.willpower
        self.dexterity += other.dexterity
        self.accuracy += other.accuracy
        self.speed += other.speed
        self.luck += other.luck
        return self
    
    def __isub__(self, other: Self) -> Self:
        if not isinstance(other, Attribute):
            raise TypeError(f"Invalid operand type: expected Attribute, got {type(other).__name__}")
        
        self.strength -= other.strength
        self.defense -= other.defense
        self.intellect -= other.intellect
        self.willpower -= other.willpower
        self.dexterity -= other.dexterity
        self.accuracy -= other.accuracy
        self.speed -= other.speed
        self.luck -= other.luck
        return self

    @property
    def strength(self):
        return self._strength

    @property
    def defense(self):
        return self._defense

    @property
    def intellect(self):
        return self._intellect

    @property
    def willpower(self):
        return self._willpower

    @property
    def dexterity(self):
        return self._dexterity

    @property
    def accuracy(self):
        return self._accuracy

    @property
    def speed(self):
        return self._speed

    @property
    def luck(self):
        return self._luck
    
    @strength.setter
    @numcheck()
    def strength(self, other: int):
        self._strength = int(other)
        
    @defense.setter
    @numcheck()
    def defense(self, other: int):
        self._defense = int(other)
        
    @intellect.setter
    @numcheck()
    def intellect(self, other: int):
        self._intellect = int(other) 

    @willpower.setter
    @numcheck()
    def willpower(self, other: int):
        self._willpower = int(other)
        
    @dexterity.setter
    @numcheck()
    def dexterity(self, other: int):
        self._dexterity = int(other)
        
    @accuracy.setter
    @numcheck()
    def accuracy(self, other: int):
        self._accuracy = int(other)
        
    @speed.setter
    @numcheck()
    def speed(self, other: int):
        self._speed = int(other)
        
    @luck.setter
    @numcheck()
    def luck(self, other: int):
        self._luck = int(other)