from dataclasses import dataclass
from typing import Optional, Self
from classes.data.datautils import numcheck
from math import floor

@dataclass
class FloatStatusModifier:
    _health: float = 0.0
    _mana: float = 0.0

    def __post_init__(self):
        # Check for type incongruency
        if not (
                isinstance(self._health, (int, float)) \
                and isinstance(self._mana, (int, float))
            ):
            raise TypeError(f"StatusPercentage init error: Attributes must be of type float")
        
        # Type conversion
        if not (
                isinstance(self._health, float) \
                and isinstance(self._mana, float)
            ):
            self._health = float(self._health)
            self._mana = float(self._mana)

    @property
    def health(self):
        return self._health
    
    @property
    def mana(self):
        return self._mana

    @health.setter
    @numcheck(val_chk=False)
    def health(self, other: int | float):
        self._health = float(other)
    
    @mana.setter
    @numcheck(val_chk=False)
    def mana(self, other: int | float):
        self._mana = float(other)


@dataclass
class IntStatusModifier:
    _health: int = 0
    _mana: int = 0
    _max_health: int = 0
    _max_mana: int = 0


    def __post_init__(self):
        # Check for type incongruency
        if not (
                isinstance(self._health, (int, float)) \
                and isinstance(self._mana, (int, float))
            ):
            raise TypeError(f"IntStatusModifier init error: Attributes must be of type int or float but given {type(self._health).__name__} and {type(self._mana).__name__}")
        
        # Type conversion
        if not (
                isinstance(self._health, int) \
                and isinstance(self._mana, int)
            ):
            self._health = floor(self._health)
            self._mana = floor(self._mana)
            self._max_health = floor(self._max_health)
            self._max_mana = floor(self._max_mana)

    @property
    def health(self):
        return self._health
    
    @property
    def mana(self):
        return self._mana

    @property
    def max_health(self):
        return self._max_health
    
    @property
    def max_mana(self):
        return self._max_mana

    @health.setter
    @numcheck(val_chk=False)
    def health(self, other: int | float):
        self._health = int(other)
    
    @mana.setter
    @numcheck(val_chk=False)
    def mana(self, other: int | float):
        self._mana = int(other)

    @max_health.setter
    @numcheck(val_chk=False)
    def max_health(self, other: int | float):
        self._max_health = int(other)

    @max_mana.setter
    @numcheck(val_chk=False)
    def max_mana(self, other: int | float):
        self._max_mana = int(other)



@dataclass
class Status:
    _health: int = 0
    _mana: int = 0

    _max_health: int = 0
    _max_mana: int = 0 
    
    # Initialization
    def __post_init__(self):
        # Check for type incongruency
        if not (
                isinstance(self._health, (int, float)) \
                and isinstance(self._mana, (int, float)) \
                and isinstance(self._max_health, (int, float)) \
                and isinstance(self._max_mana, (int, float))
           ):
            raise TypeError(f"Status init error: Attributes must be of type int or float")
        
        # Int conversion
        if isinstance(self._health, float) \
           or isinstance(self._mana, float) \
           or isinstance(self._max_health, float) \
           or isinstance(self._max_mana, float):
            self._health = floor(self._health)
            self._mana = floor(self._mana)
            self._max_health = floor(self._max_health)
            self._max_mana = floor(self._max_mana)


        # Check for invalid values
        if not (
                self._health >= 0 \
                and self._mana >= 0 \
                and self._max_health >= 0 \
                and self._max_mana >= 0
            ):
            raise ValueError(f"Status init error: Attributes must be non-negative")
        
        # Overflow handling
        if self._health > self._max_health:
            self._health = self._max_health

        if self._mana > self._max_mana:
            self._mana = self._max_mana


    # Status Arithmetic
    def __add__(self, other: IntStatusModifier) -> Self:
        if not isinstance(other, IntStatusModifier):
            raise TypeError(f"Invalid operand type: expected Status, got {type(other).__name__}")

        current_type = type(self)
        new_health = self.health + other.health
        new_max_health = self.max_health + other.max_health
        new_mana = self.mana + other.mana
        new_max_mana = self.max_mana + other.max_mana
        return current_type(new_health, new_mana, new_max_health, new_max_mana)
    
    def __sub__(self, other: IntStatusModifier) -> Self:
        if not isinstance(other, IntStatusModifier):
            raise TypeError(f"Invalid operand type: expected Status, got {type(other).__name__}")
        
        current_type = type(self)
        new_health = self.health - other.health
        new_max_health = self.max_health - other.max_health
        new_mana = self.mana - other.mana
        new_max_mana = self.max_mana - other.max_mana
        return current_type(new_health, new_mana, new_max_health, new_max_mana)
        
    def __iadd__(self, other: IntStatusModifier) -> Self:
        if not isinstance(other, IntStatusModifier):
            raise TypeError(f"Invalid operand type: expected Status, got {type(other).__name__}")
        
        self.max_health += other.max_health
        self.max_mana += other.max_mana
        
        self.health = min(self.health + other.health, self.max_health)
        self.mana = min(self.mana + other.mana, self.max_mana)
        return self
        
    def __isub__(self, other: IntStatusModifier) -> Self:
        if not isinstance(other, IntStatusModifier):
            raise TypeError(f"Invalid operand type: expected Status, got {type(other).__name__}")
        
        self.max_health -= other.max_health
        self.max_mana -= other.max_mana

        self.health = min(self.health - other.health, self.max_health)
        self.mana = min(self.mana - other.mana, self.max_mana)
        return self

    def __imul__(self, other: FloatStatusModifier) -> Self:
        if not isinstance(other, FloatStatusModifier):
            raise TypeError(f"Invalid operand type: expected FloatStatusModifier, got {type(other).__name__}")
        
        self.health += int(other.health * self.max_health)
        self.mana += int(other.mana * self.max_mana)
        return self
    
    
    @property
    def health(self):
        return self._health
    
    @property
    def max_health(self):
        return self._max_health
    
    @property
    def mana(self):
        return self._mana
    
    @property
    def max_mana(self):
        return self._max_mana
    
    @health.setter
    @numcheck()
    def health(self, other: int | float):
        self._health = int(min(other, self._max_health))
    
    @max_health.setter
    @numcheck()
    def max_health(self, other: int | float):
        self._max_health = int(other)

    @mana.setter
    @numcheck()
    def mana(self, other: int | float):
        self._mana = int(min(other, self._max_mana))
    
    @max_mana.setter
    @numcheck()
    def max_mana(self, other: int | float):
        self._max_mana = int(other)
