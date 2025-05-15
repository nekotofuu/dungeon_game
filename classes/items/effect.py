from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod

class ItemEffect(ABC):
    @abstractmethod
    def __call__(self, target, **parameters):
        pass
