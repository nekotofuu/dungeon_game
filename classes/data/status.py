from typing import Optional, Self
from classes.data.utils import numcheck
from math import floor


class StatusModifier:
    _health: int | float = 0
    _mana: int | float = 0
    _max_health: int | float = 0
    _max_mana: int | float = 0
    _frac: bool = False

    def __init__(
            self, 
            health: int | float = 0, 
            mana: int | float = 0, 
            max_health: int | float = 0, 
            max_mana: int | float = 0, 
            frac: bool = False
            ) -> None:
        self._frac = frac
        
        if not (
                isinstance(health, (int, float)) \
                and isinstance(mana, (int, float)) \
                and isinstance(max_health, (int, float)) \
                and isinstance(max_mana, (int, float))
            ):
            raise TypeError("Attributes must be of type int or float.")
        
        # Type conversion
        if (frac):
            self._health = float(health)
            self._mana = float(mana)
            self._max_health = float(max_health)
            self._max_mana = float(max_mana)
        else:
            self._health = int(health)
            self._mana = int(mana)
            self._max_health = int(max_health)
            self._max_mana = int(max_mana)

    def __str__(self) -> str:
        if self.integer:
            return f"{self.health:+d}/{self.mana:+d} ({self.max_health:+d}/{self.max_mana:+d})"
        else:
            return f"{self.health:+.0%}/{self.mana:+.0%} ({self.max_health:+.0%}/{self.max_mana:+.0%})"

    def __repr__(self) -> str:
        return f"StatusModifier(health={self.health}, mana={self.mana}, max_health={self.max_health}, max_mana={self.max_mana}, frac={self.fractional})"

    def __add__(self, other: Self) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")

        # Check for conflicting modification types
        if self.integer ^ other.integer:
            raise ValueError(f"Invalid value: Operation only accepts same type of StatusModifier")

        current_type = type(self)

        new_health = self.health + other.health
        new_mana = self.mana + other.mana
        new_max_health = self.max_health + other.max_health
        new_max_mana = self.max_mana + other.max_mana

        result = current_type(new_health, new_mana, new_max_health, new_max_mana, self.fractional)
        return round(result)

    def __sub__(self, other: Self) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")

        # Check for conflicting modification types
        if self.integer ^ other.integer:
            raise ValueError(f"Invalid value: Operation only accepts same type of StatusModifier")

        current_type = type(self)

        new_health = self.health - other.health
        new_mana = self.mana - other.mana
        new_max_health = self.max_health - other.max_health
        new_max_mana = self.max_mana - other.max_mana

        result = current_type(new_health, new_mana, new_max_health, new_max_mana, self.fractional)
        return round(result)
    
    def __iadd__(self, other: Self) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")

        # Check for conflicting modification types
        if self.integer ^ other.integer:
            raise ValueError(f"Invalid value: Operation only accepts same type of StatusModifier")

        self.health += other.health
        self.mana += other.mana
        self.max_health += other.max_health
        self.max_mana += other.max_mana
        return round(self)

    def __isub__(self, other: Self) -> Self:
        # Check for type incongruency
        if not isinstance(other, StatusModifier):
            raise TypeError(f"Invalid operand type: expected StatusModifier, got {type(other).__name__}")

        # Check for conflicting modification types
        if self.integer ^ other.integer:
            raise ValueError(f"Invalid value: Operation only accepts same type of StatusModifier")

        self.health -= other.health
        self.mana -= other.mana
        self.max_health -= other.max_health
        self.max_mana -= other.max_mana
        return round(self)

    def __round__(self) -> Self:
        if self.integer:
            return self
        else:
            self.health = round(self.health, 4)
            self.mana = round(self.mana, 4)
            self.max_health = round(self.max_health, 4)
            self.max_mana = round(self.max_mana, 4)
            return self

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



class Status:
    # Initialization
    def __init__(
            self,
            health: int = 0,
            mana: int = 0,
            max_health: int = 0,
            max_mana: int = 0,
            ) -> None:
        
        # Check for invalid values
        if not (
                health >= 0 \
                and mana >= 0 \
                and max_health >= 0 \
                and max_mana >= 0
            ):
            raise ValueError(f"Status init error: Attributes must be non-negative")

        # Check for type incongruency
        if not (
                isinstance(health, (int, float)) \
                and isinstance(mana, (int, float)) \
                and isinstance(max_health, (int, float)) \
                and isinstance(max_mana, (int, float))
           ):
            raise TypeError(f"Status init error: Attributes must be of type int or float")
        
        self._health = floor(health)
        self._mana = floor(mana)
        self._max_health = floor(max_health)
        self._max_mana = floor(max_mana)
        
        # Overflow handling
        if self.health > self.max_health:
            self.health = self.max_health

        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def __str__(self) -> str:
        return f"{self.health:d}/{self.mana:d} ({self.max_health:d}/{self.max_mana:d})"

    def __repr__(self) -> str:
        return f"Status(health={self.health}, mana={self.mana}, max_health={self.max_health}, max_mana={self.max_mana})"

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
