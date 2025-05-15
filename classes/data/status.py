from dataclasses import dataclass
from typing import Optional, Self
from classes.data.datautils import numcheck
from math import floor

@dataclass
class StatusModifier:
    _health: int | float = 0
    _mana: int | float = 0
    _max_health: int | float = 0
    _max_mana: int | float = 0
    _frac: bool = False

    def __post_init__(self):
        # Check for type incongruency
        if not (
                isinstance(self._health, (int, float)) \
                and isinstance(self._mana, (int, float)) \
                and isinstance(self._max_health, (int, float)) \
                and isinstance(self._max_mana, (int, float))
            ):
            raise TypeError("Attributes must be of type int or float.")
        
        # Type conversion
        if (self._frac):
            self._health = float(self._health)
            self._mana = float(self._mana)
            self._max_health = float(self._max_health)
            self._max_mana = float(self._max_mana)
        else:
            self._health = int(self._health)
            self._mana = int(self._mana)
            self._max_health = int(self._max_health)
            self._max_mana = int(self._max_mana)

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
    
    @property
    def fractional(self):
        return self._frac
    
    @property
    def integer(self):
        return not self._frac

    @health.setter
    @numcheck(val_chk=False)
    def health(self, other: int | float):
        if self.integer:
            convert_type = int
        else:
            convert_type = float
        
        self._health = convert_type(other)
    
    @mana.setter
    @numcheck(val_chk=False)
    def mana(self, other: int | float):
        if self.integer:
            convert_type = int
        else:
            convert_type = float

        self._mana = convert_type(other)

    @max_health.setter
    @numcheck(val_chk=False)
    def max_health(self, other: int | float):
        if self.integer:
            convert_type = int
        else:
            convert_type = float

        self._max_health = convert_type(other)

    @max_mana.setter
    @numcheck(val_chk=False)
    def max_mana(self, other: int | float):
        if self.integer:
            convert_type = int
        else:
            convert_type = float
        
        self._max_mana = convert_type(other)

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
    def __add__(self, other: StatusModifier) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected Status, got {type(other).__name__}")

        # Check for valid values
        if other.fractional:
            raise ValueError(f"Invalid value: Status only accepts integer StatusModifier")

        current_type = type(self)

        new_max_health = int(self.max_health + other.max_health)
        new_max_mana = int(self.max_mana + other.max_mana)

        new_health = int(min(self.health + other.health, new_max_health))
        new_mana = int(min(self.mana + other.mana, new_max_mana))

        return current_type(new_health, new_mana, new_max_health, new_max_mana)
    
    def __sub__(self, other: StatusModifier) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")
        
        # Check for valid values
        if other.fractional:
            raise ValueError(f"Invalid value: Status only accepts integer StatusModifier")

        current_type = type(self)

        new_max_health = int(self.max_health - other.max_health)
        new_max_mana = int(self.max_mana - other.max_mana)

        new_health = int(min(self.health - other.health, new_max_health))
        new_mana = int(min(self.mana - other.mana, new_max_mana))
        
        return current_type(new_health, new_mana, new_max_health, new_max_mana)
        
    def __mul__(self, other: StatusModifier) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")
        
        # Check for valid values
        if other.integer:
            raise ValueError(f"Invalid value: Status only accepts integer StatusModifier")
        
        current_type = type(self)

        new_max_health = int(self.max_health * (1 + other.max_health))
        new_max_mana = int(self.max_mana * (1 + other.max_mana))

        new_health = int(min(self.health + self.max_health * other.health, new_max_health))
        new_mana = int(min(self.mana + self.max_mana * other.mana, new_max_mana))
        return current_type(new_health, new_mana, new_max_health, new_max_mana)

    def __iadd__(self, other: StatusModifier) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")
        
        # Check for valid values
        if other.fractional:
            raise ValueError(f"Invalid value: Status only accepts integer StatusModifier")
        
        self.max_health += other.max_health
        self.max_mana += other.max_mana
        
        self.health = min(self.health + other.health, self.max_health)
        self.mana = min(self.mana + other.mana, self.max_mana)
        return self
        
    def __isub__(self, other: StatusModifier) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")
        
        # Check for valid values
        if other.fractional:
            raise ValueError(f"Invalid value: Status only accepts integer StatusModifier")
        
        self.max_health -= other.max_health
        self.max_mana -= other.max_mana

        self.health = min(self.health - other.health, self.max_health)
        self.mana = min(self.mana - other.mana, self.max_mana)
        return self

    def __imul__(self, other: StatusModifier) -> Self:
        
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")
        
        # Check for valid values
        if other.integer:
            raise ValueError(f"Invalid value: Status only accepts float StatusModifier")
        
        self.max_health *= 1 + other.max_health
        self.max_mana *= 1 + other.max_mana
        
        self.health = min(self.health + self.max_health * other.health, self.max_health)
        self.mana = min(self.mana + self.max_mana * other.mana, self.max_mana)
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

        if self._health > self._max_health:
            self._health = self._max_health

    @mana.setter
    @numcheck()
    def mana(self, other: int | float):
        self._mana = int(min(other, self._max_mana))
    
    @max_mana.setter
    @numcheck()
    def max_mana(self, other: int | float):
        self._max_mana = int(other)

        if self._mana > self._max_mana:
            self._mana = self._max_mana
