from classes.metadata import *
from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod
from classes.items.effect import *

"""
Contains classes related to 
Item types, classes, and instantiation
"""

@dataclass
class Item:
    metadata: Metadata

class ItemCreator:
    pass

class Usable(Item, ABC):
    def __init__(self, metadata: Metadata):
        super().__init__(metadata)
        #item_effect: ItemEffect
        #effect_parameter: Tuple[Any]
        pass

    @abstractmethod
    def use(self):
        pass

class Equippable(Item, ABC):
    def __init__(self, Metadata):
        #attr_mod: Attribute
        #skill_set: List[Skill]
        pass
