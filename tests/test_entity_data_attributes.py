# type: ignore

import pytest
from classes.data.attributes import Attribute

def test_attribute_init():
    # Normal case
    a = Attribute(1, 2, 3, 4, 5, 5, 6, 7)
    assert a.strength == 1
    assert a.defense == 2
    assert a.intellect == 3
    assert a.willpower == 4
    assert a.dexterity == 5
    assert a.accuracy == 5
    assert a.speed == 6
    assert a.luck == 7

    # Default case
    a = Attribute()
    assert a.strength == 0
    assert a.defense == 0
    assert a.intellect == 0
    assert a.willpower == 0
    assert a.dexterity == 0
    assert a.accuracy == 0
    assert a.speed == 0
    assert a.luck == 0

    a = Attribute(_strength=2, _willpower=3, _luck=5)
    assert a.strength == 2
    assert a.defense == 0
    assert a.intellect == 0
    assert a.willpower == 3
    assert a.dexterity == 0
    assert a.accuracy == 0
    assert a.speed == 0
    assert a.luck == 5

    a = Attribute(0.1, 1.2, 2.3, 5.4, 10.5, 7.6, 3.7, 9.8)
    assert a.strength == 0
    assert a.defense == 1
    assert a.intellect == 2
    assert a.willpower == 5
    assert a.dexterity == 10
    assert a.accuracy == 7
    assert a.speed == 3
    assert a.luck == 9

    # Error case
    with pytest.raises(ValueError):
        Attribute(10, 2, 3, 9, -1, 0 ,2, 0)
    
def test_attribute_add():
    # Addition
    ## All
    a1 = Attribute(1, 2, 3, 4, 5, 6, 7, 8)
    a2 = Attribute(2, 4, 6, 8, 10, 12, 14, 16)
    a3 = a1 + a2
    assert a3.strength == 3
    assert a3.defense == 6
    assert a3.intellect == 9
    assert a3.willpower == 12
    assert a3.dexterity == 15
    assert a3.accuracy == 18
    assert a3.speed == 21
    assert a3.luck == 24
    
    ## Partial
    a1 = Attribute(7, 33, 41, 16, 25, 95, 17, 77)
    a2 = Attribute(_defense=7, _intellect=33, _accuracy=20)
    a3 = a1 + a2
    assert a3.strength == 7
    assert a3.defense == 40
    assert a3.intellect == 74
    assert a3.willpower == 16
    assert a3.dexterity == 25
    assert a3.accuracy == 115
    assert a3.speed == 17
    assert a3.luck == 77

    # Assignment
    ## All
    a1 = Attribute(1, 2, 3, 4, 5, 6, 7, 8)
    a1 += Attribute(2, 4, 6, 8, 10, 12, 14, 16)
    assert a1.strength == 3
    assert a1.defense == 6
    assert a1.intellect == 9
    assert a1.willpower == 12
    assert a1.dexterity == 15
    assert a1.accuracy == 18
    assert a1.speed == 21
    assert a1.luck == 24
    
    ## Partial
    a1 = Attribute(7, 33, 41, 16, 25, 95, 17, 77)
    a1 += Attribute(_defense=7, _intellect=33, _accuracy=20)
    assert a1.strength == 7
    assert a1.defense == 40
    assert a1.intellect == 74
    assert a1.willpower == 16
    assert a1.dexterity == 25
    assert a1.accuracy == 115
    assert a1.speed == 17
    assert a1.luck == 77

def test_attribute_sub():
    # Subtraction
    ## All
    a1 = Attribute(100, 100, 100, 100, 100, 100, 100, 100)
    a2 = Attribute(41, 14, 61, 75, 80, 43, 98, 27)
    a3 = a1 - a2
    assert a3.strength == 59
    assert a3.defense == 86
    assert a3.intellect == 39
    assert a3.willpower == 25
    assert a3.dexterity == 20
    assert a3.accuracy == 57
    assert a3.speed == 2
    assert a3.luck == 73

    ## Partial
    a1 = Attribute(100, 100, 100, 100, 100, 100, 100, 100)
    a2 = Attribute(_intellect=12, _speed=10, _dexterity=99)
    a3 = a1 - a2
    assert a3.strength == 100
    assert a3.defense == 100
    assert a3.intellect == 88
    assert a3.willpower == 100
    assert a3.dexterity == 1
    assert a3.accuracy == 100
    assert a3.speed == 90
    assert a3.luck == 100

    # Assignment
    ## All
    a = Attribute(100, 100, 100, 100, 100, 100, 100, 100)
    a -= Attribute(41, 14, 61, 75, 80, 43, 98, 27)
    assert a.strength == 59
    assert a.defense == 86
    assert a.intellect == 39
    assert a.willpower == 25
    assert a.dexterity == 20
    assert a.accuracy == 57
    assert a.speed == 2
    assert a.luck == 73

    ## Partial
    a = Attribute(100, 100, 100, 100, 100, 100, 100, 100)
    a -= Attribute(_intellect=12, _speed=10, _dexterity=99)
    assert a.strength == 100
    assert a.defense == 100
    assert a.intellect == 88
    assert a.willpower == 100
    assert a.dexterity == 1
    assert a.accuracy == 100
    assert a.speed == 90
    assert a.luck == 100
