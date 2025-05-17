# type: ignore

import pytest
from classes.data.attributes import Attribute

def test_attr_init():
    # Test default initialization
    attr = Attribute()
    assert attr.strength == 0
    assert attr.defense == 0
    assert attr.intellect == 0
    assert attr.willpower == 0
    assert attr.dexterity == 0
    assert attr.accuracy == 0
    assert attr.speed == 0
    assert attr.luck == 0

    # Custom initialization with valid values
    attr = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    assert attr.strength == 10
    assert attr.defense == 20
    assert attr.intellect == 30
    assert attr.willpower == 40
    assert attr.dexterity == 50
    assert attr.accuracy == 60
    assert attr.speed == 70
    assert attr.luck == 80

    # Test initialization with float values
    attr = Attribute(strength=10.5, defense=20.5, intellect=30.5, willpower=40.5, dexterity=50.5, accuracy=60.5, speed=70.5, luck=80.5)
    assert attr.strength == 10
    assert attr.defense == 20
    assert attr.intellect == 30
    assert attr.willpower == 40
    assert attr.dexterity == 50
    assert attr.accuracy == 60
    assert attr.speed == 70
    assert attr.luck == 80

    # Invalid initialization with negative values
    with pytest.raises(ValueError):
        Attribute(-1, -2, -3, -4, -5, -6, -7, -8)

    # Invalid initialization with non-integer types
    with pytest.raises(TypeError):
        Attribute("a", "b", "c", "d", "e", "f", "g", "h")
    
    # Invalid initialization with mixed types
    with pytest.raises(TypeError):
        Attribute(1, 2, 3.5, 4, 5, 6, 7, "8")
    
def test_attr_str():
    # Test string representation
    attr = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    expected_str = "STR: 10\nDEF: 20\nINT: 30\nWIL: 40\nDEX: 50\nACC: 60\nSPD: 70\nLCK: 80"
    assert str(attr) == expected_str

def test_attr_repr():
    # Test repr representation
    attr = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    expected_repr = "Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)"
    assert repr(attr) == expected_repr

def test_attr_add():
    # Test addition of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = Attribute(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
    result = attr1 + attr2

    assert result.strength == 15
    assert result.defense == 30
    assert result.intellect == 45
    assert result.willpower == 60
    assert result.dexterity == 75
    assert result.accuracy == 90
    assert result.speed == 105
    assert result.luck == 120

    # Test addition with a non-Attribute object
    with pytest.raises(TypeError):
        attr1 + "not an attribute"

    # Test addition with an empty Attribute
    attr_empty = Attribute()
    result = attr1 + attr_empty
    assert result.strength == 10
    assert result.defense == 20
    assert result.intellect == 30
    assert result.willpower == 40
    assert result.dexterity == 50
    assert result.accuracy == 60
    assert result.speed == 70
    assert result.luck == 80

def test_attr_sub():
    # Test subtraction of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = Attribute(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
    result = attr1 - attr2

    assert result.strength == 5
    assert result.defense == 10
    assert result.intellect == 15
    assert result.willpower == 20
    assert result.dexterity == 25
    assert result.accuracy == 30
    assert result.speed == 35
    assert result.luck == 40

    # Test subtraction with a non-Attribute object
    with pytest.raises(TypeError):
        attr1 - "not an attribute"

    # Test subtraction with an empty Attribute
    attr_empty = Attribute()
    result = attr1 - attr_empty
    assert result.strength == 10
    assert result.defense == 20
    assert result.intellect == 30
    assert result.willpower == 40
    assert result.dexterity == 50
    assert result.accuracy == 60
    assert result.speed == 70
    assert result.luck == 80

def test_attr_iadd():
    # Test in-place addition of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = Attribute(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
    attr1 += attr2

    assert attr1.strength == 15
    assert attr1.defense == 30
    assert attr1.intellect == 45
    assert attr1.willpower == 60
    assert attr1.dexterity == 75
    assert attr1.accuracy == 90
    assert attr1.speed == 105
    assert attr1.luck == 120

    # Test in-place addition with a non-Attribute object
    with pytest.raises(TypeError):
        attr1 += "not an attribute"
    
    # Test in-place addition with an empty Attribute
    attr_empty = Attribute()
    attr1 += attr_empty
    assert attr1.strength == 15
    assert attr1.defense == 30
    assert attr1.intellect == 45
    assert attr1.willpower == 60
    assert attr1.dexterity == 75
    assert attr1.accuracy == 90
    assert attr1.speed == 105
    assert attr1.luck == 120

def test_attr_isub():
    # Test in-place subtraction of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = Attribute(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
    attr1 -= attr2

    assert attr1.strength == 5
    assert attr1.defense == 10
    assert attr1.intellect == 15
    assert attr1.willpower == 20
    assert attr1.dexterity == 25
    assert attr1.accuracy == 30
    assert attr1.speed == 35
    assert attr1.luck == 40

    # Test in-place subtraction with a non-Attribute object
    with pytest.raises(TypeError):
        attr1 -= "not an attribute"
    
    # Test in-place subtraction with an empty Attribute
    attr_empty = Attribute()
    attr1 -= attr_empty
    assert attr1.strength == 5
    assert attr1.defense == 10
    assert attr1.intellect == 15
    assert attr1.willpower == 20
    assert attr1.dexterity == 25
    assert attr1.accuracy == 30
    assert attr1.speed == 35
    assert attr1.luck == 40