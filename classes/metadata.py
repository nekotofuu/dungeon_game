from dataclasses import dataclass

"""
Comtains essential classes 
for housing instance data.
"""

@dataclass
class Metadata:
    """
    Class that represents 
    identifier information for a data object
    """
    id: str
    name: str
    description: str