from typing import Self
from classes.data.utils import numcheck

class AttributeModifier:
    # Initialization
    def __init__(
            self,
            strength: int | float = 0,
            defense: int | float = 0,
            intellect: int | float = 0,
            willpower: int | float = 0,
            dexterity: int | float = 0,
            accuracy: int | float = 0,
            speed: int | float = 0,
            luck: int | float = 0,
            frac: bool = False  
        ) -> None:
        self._frac = frac
        
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
            raise TypeError(f"Attributes must be of type int")

        if self._frac:
            self._strength = float(strength)
            self._defense = float(defense)
            self._intellect = float(intellect)
            self._willpower = float(willpower)
            self._dexterity = float(dexterity)
            self._accuracy = float(accuracy)
            self._speed = float(speed)
            self._luck = float(luck)
        else:
            self._strength = int(strength)
            self._defense = int(defense)
            self._intellect = int(intellect)
            self._willpower = int(willpower)
            self._dexterity = int(dexterity)
            self._accuracy = int(accuracy)
            self._speed = int(speed)
            self._luck = int(luck)

    def __str__(self) -> str:
        if self.isinteger:
            return f"STR/DEF/INT/WIL/DEX/ACC/SPD/LCK: ({self.strength:+d}/{self.defense:+d}/{self.intellect:+d}/{self.willpower:+d}/" \
                   f"{self.dexterity:+d}/{self.accuracy:+d}/{self.speed:+d}/{self.luck:+d})"
        else:
            return f"STR/DEF/INT/WIL/DEX/ACC/SPD/LCK: ({self.strength:+.0%}/{self.defense:+.0%}/{self.intellect:+.0%}/" \
                   f"{self.willpower:+.0%}/{self.dexterity:+.0%}/{self.accuracy:+.0%}/{self.speed:+.0%}/{self.luck:+.0%})"

    def __repr__(self) -> str:
        return f"Attribute(strength={self.strength}, defense={self.defense}, intellect={self.intellect}, " \
               f"willpower={self.willpower}, dexterity={self.dexterity}, accuracy={self.accuracy}, speed={self.speed}, " \
               f"luck={self.luck}, frac={self.isfractional})"
    
    def __add__(self, other: Self) -> Self:
        # Check for type inconsistencies
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operation: Expected AttributeModifier but got {type(other).__name__}")
        
        if self.isinteger ^ other.isinteger:
            raise ValueError(f"Invalid value: Operation only accepts AttributeModifier of the same type")
        
        ctype = type(self)
        new_strength = self.strength + other.strength
        new_defense = self.defense + other.defense
        new_intellect = self.intellect + other.intellect
        new_willpower = self.willpower + other.willpower
        new_dexterity = self.dexterity + other.dexterity
        new_accuracy = self.accuracy + other.accuracy
        new_speed = self.speed + other.speed
        new_luck = self.luck + other.luck
        result = ctype(new_strength, new_defense, new_intellect, new_willpower, new_dexterity, new_accuracy, new_speed, new_luck, self.isfractional)
        return round(result)

    def __sub__(self, other: Self) -> Self:
        # Check for type inconsistencies
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operation: Expected AttributeModifier but got {type(other).__name__}")
        
        if self.isinteger ^ other.isinteger:
            raise ValueError(f"Invalid value: Operation only accepts AttributeModifier of the same type")
        
        ctype = type(self)
        new_strength = self.strength - other.strength
        new_defense = self.defense - other.defense
        new_intellect = self.intellect - other.intellect
        new_willpower = self.willpower - other.willpower
        new_dexterity = self.dexterity - other.dexterity
        new_accuracy = self.accuracy - other.accuracy
        new_speed = self.speed - other.speed
        new_luck = self.luck - other.luck
        result = ctype(new_strength, new_defense, new_intellect, new_willpower, new_dexterity, new_accuracy, new_speed, new_luck, self.isfractional)
        return round(result)

    def __iadd__(self, other: Self) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operation: Expected AttributeModifier but got {type(other).__name__}")
        
        if self.isinteger ^ other.isinteger:
            raise ValueError(f"Invalid value: Operation only accepts AttributeModifier of the same type")
        
        self.strength += other.strength
        self.defense += other.defense
        self.intellect += other.intellect
        self.willpower += other.willpower
        self.dexterity += other.dexterity
        self.accuracy += other.accuracy
        self.speed += other.speed
        self.luck += other.luck
        return round(self)
    
    def __isub__(self, other: Self) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operation: Expected AttributeModifier but got {type(other).__name__}")
        
        if self.isinteger ^ other.isinteger:
            raise ValueError(f"Invalid value: Operation only accepts AttributeModifier of the same type")
        
        self.strength -= other.strength
        self.defense -= other.defense
        self.intellect -= other.intellect
        self.willpower -= other.willpower
        self.dexterity -= other.dexterity
        self.accuracy -= other.accuracy
        self.speed -= other.speed
        self.luck -= other.luck
        return round(self)

    def __round__(self) -> Self:
        if self.isinteger:
            return self
        else:
            self.strength = round(self.strength, 4)
            self.defense = round(self.defense, 4)
            self.intellect = round(self.intellect, 4)
            self.willpower = round(self.willpower, 4)
            self.dexterity = round(self.dexterity, 4)
            self.accuracy = round(self.accuracy, 4)
            self.speed = round(self.speed, 4)
            self.luck = round(self.luck, 4)
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
    
    @property
    def isfractional(self):
        return self._frac
    
    @property
    def isinteger(self):
        return not self._frac
    
    @property
    def type(self):
        if self._frac:
            return float
        else:
            return int
    
    @strength.setter
    @numcheck(val_chk=False)
    def strength(self, other: int | float):
        self._strength = self.type(other)
        
    @defense.setter
    @numcheck(val_chk=False)
    def defense(self, other: int | float):
        self._defense = self.type(other)
        
    @intellect.setter
    @numcheck(val_chk=False)
    def intellect(self, other: int | float):
        self._intellect = self.type(other) 

    @willpower.setter
    @numcheck(val_chk=False)
    def willpower(self, other: int | float):
        self._willpower = self.type(other)
        
    @dexterity.setter
    @numcheck(val_chk=False)
    def dexterity(self, other: int | float):
        self._dexterity = self.type(other)
        
    @accuracy.setter
    @numcheck(val_chk=False)
    def accuracy(self, other: int | float):
        self._accuracy = self.type(other)
        
    @speed.setter
    @numcheck(val_chk=False)
    def speed(self, other: int | float):
        self._speed = self.type(other)
        
    @luck.setter
    @numcheck(val_chk=False)
    def luck(self, other: int | float):
        self._luck = self.type(other)

class Attribute:
    # Initialization
    def __init__(
            self,
            strength: int | float = 0,
            defense: int | float = 0,
            intellect: int | float = 0,
            willpower: int | float = 0,
            dexterity: int | float = 0,
            accuracy: int | float = 0,
            speed: int | float = 0,
            luck: int | float = 0    
        ) -> None:
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
            raise TypeError(f"Attributes must be of type int")
        
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
            raise ValueError(f"Attributes must be non-negative")
        
        self._strength = int(strength)
        self._defense = int(defense)
        self._intellect = int(intellect)
        self._willpower = int(willpower)
        self._dexterity = int(dexterity)
        self._accuracy = int(accuracy)
        self._speed = int(speed)
        self._luck = int(luck)
    
    def __str__(self) -> str:
        return f"STR/DEF/INT/WIL/DEX/ACC/SPD/LCK: ({self.strength}/{self.defense}/{self.intellect}/{self.willpower}/{self.dexterity}/{self.accuracy}/{self.speed}/{self.luck})"

    def __repr__(self) -> str:
        return f"Attribute(strength={self.strength}, defense={self.defense}, intellect={self.intellect}, willpower={self.willpower}, dexterity={self.dexterity}, accuracy={self.accuracy}, speed={self.speed}, luck={self.luck})"
    
    def __add__(self, other: AttributeModifier) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operand type: expected AttributeModifier, got {type(other).__name__}")

        if other.isfractional:
            raise ValueError(f"Invalid modifier type: expected integer")

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

    def __sub__(self, other: AttributeModifier) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operand type: expected AttributeModifier, got {type(other).__name__}")
        
        if other.isfractional:
            raise ValueError(f"Invalid modifier type: expected integer")

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

    def __mul__(self, other: AttributeModifier) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operand type: expected AttributeModifier, got {type(other).__name__}")
        
        if other.isinteger:
            raise ValueError(f"Invalid modifier type: expected fractional")

        ctype = type(self)
        new_strength = int(round(self.strength * (1 + other.strength)))
        new_defense = int(round(self.defense * (1 + other.defense)))
        new_intellect = int(round(self.intellect * (1 + other.intellect)))
        new_willpower = int(round(self.willpower * (1 + other.willpower)))
        new_dexterity = int(round(self.dexterity * (1 + other.dexterity)))
        new_accuracy = int(round(self.accuracy * (1 + other.accuracy)))
        new_speed = int(round(self.speed * (1 + other.speed)))
        new_luck = int(round(self.luck * (1 + other.luck)))

        return ctype(new_strength, new_defense, new_intellect, new_willpower, new_dexterity, new_accuracy, new_speed, new_luck)

    def __iadd__(self, other: AttributeModifier) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operand type: expected AttributeModifier, got {type(other).__name__}")
        
        if other.isfractional:
            raise ValueError(f"Invalid modifier type: expected integer")

        self.strength += int(other.strength)
        self.defense += int(other.defense)
        self.intellect += int(other.intellect)
        self.willpower += int(other.willpower)
        self.dexterity += int(other.dexterity)
        self.accuracy += int(other.accuracy)
        self.speed += int(other.speed)
        self.luck += int(other.luck)
        return self
    
    def __isub__(self, other: AttributeModifier) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operand type: expected AttributeModifier, got {type(other).__name__}")
        
        if other.isfractional:
            raise ValueError(f"Invalid modifier type: expected integer")

        self.strength -= int(other.strength)
        self.defense -= int(other.defense)
        self.intellect -= int(other.intellect)
        self.willpower -= int(other.willpower)
        self.dexterity -= int(other.dexterity)
        self.accuracy -= int(other.accuracy)
        self.speed -= int(other.speed)
        self.luck -= int(other.luck)
        return self
    
    def __imul__(self, other: AttributeModifier) -> Self:
        if not isinstance(other, AttributeModifier):
            raise TypeError(f"Invalid operand type: expected AttributeModifier, got {type(other).__name__}")
        
        if other.isinteger:
            raise ValueError(f"Invalid modifier type: expected fractional")

        self.strength = int(round(self.strength * (1 + other.strength)))
        self.defense = int(round(self.defense * (1 + other.defense)))
        self.intellect = int(round(self.intellect * (1 + other.intellect)))
        self.willpower = int(round(self.willpower * (1 + other.willpower)))
        self.dexterity = int(round(self.dexterity * (1 + other.dexterity)))
        self.accuracy = int(round(self.accuracy * (1 + other.accuracy)))
        self.speed = int(round(self.speed * (1 + other.speed)))
        self.luck = int(round(self.luck * (1 + other.luck)))
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