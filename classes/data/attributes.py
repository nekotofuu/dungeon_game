from dataclasses import dataclass
from typing import Optional, Self
from classes.data.datautils import numcheck
from math import floor


@dataclass
class Attribute:
    _strength: int = 0
    _defense: int = 0
    _intellect: int = 0
    _willpower: int = 0
    _dexterity: int = 0
    _accuracy: int = 0
    _speed: int = 0
    _luck: int = 0


    # Initialization
    def __post_init__(self):
        # Check for type incongruency
        if not (
                isinstance(self._strength, (int, float)) \
                and isinstance(self._defense, (int, float)) \
                and isinstance(self._intellect, (int, float)) \
                and isinstance(self._willpower, (int, float)) \
                and isinstance(self._dexterity, (int, float)) \
                and isinstance(self._accuracy, (int, float)) \
                and isinstance(self._speed, (int, float)) \
                and isinstance(self._luck, (int, float))
            ):
            raise TypeError(f"Attribute init error: Attributes must be of type int")
        
        # Type conversion
        if isinstance(self._strength, float) \
           or isinstance(self._defense, float) \
           or isinstance(self._intellect, float) \
           or isinstance(self._willpower, float) \
           or isinstance(self._dexterity, float) \
           or isinstance(self._accuracy, float) \
           or isinstance(self._speed, float) \
           or isinstance(self._luck, float):
            self._strength = floor(self._strength)
            self._defense = floor(self._defense)
            self._intellect = floor(self._intellect)
            self._willpower = floor(self._willpower)
            self._dexterity = floor(self._dexterity)
            self._accuracy = floor(self._accuracy)
            self._speed = floor(self._speed)
            self._luck = floor(self._luck)

        # Check for invalid values
        if not (self._strength >= 0 \
                and self._defense >= 0 \
                and self._intellect >= 0 \
                and self._willpower >= 0 \
                and self._dexterity >= 0 \
                and self._accuracy >= 0 \
                and self._speed >= 0 \
                and self._luck >= 0
            ):  
            raise ValueError(f"Attribute init error: Attributes must be non-negative")
    
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