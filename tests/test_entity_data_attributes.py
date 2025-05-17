# type: ignore

import pytest
from classes.data.attributes import Attribute, AttributeModifier

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
    expected_str = "STR/DEF/INT/WIL/DEX/ACC/SPD/LCK: (10/20/30/40/50/60/70/80)"
    assert str(attr) == expected_str

def test_attr_repr():
    # Test repr representation
    attr = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    expected_repr = "Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)"
    assert repr(attr) == expected_repr

def test_attr_add():
    # Test addition of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = AttributeModifier(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
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
    attr_empty = AttributeModifier()
    result = attr1 + attr_empty
    assert result.strength == 10
    assert result.defense == 20
    assert result.intellect == 30
    assert result.willpower == 40
    assert result.dexterity == 50
    assert result.accuracy == 60
    assert result.speed == 70
    assert result.luck == 80

    # Modifier type mismatch
    attr_float = AttributeModifier(1.2, 3.4, 5.6, 7.8, 9.1, 2.3, 4.5, 6.7, frac=True)
    with pytest.raises(ValueError):
        attr1 + attr_float

def test_attr_sub():
    # Test subtraction of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = AttributeModifier(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
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
    attr_empty = AttributeModifier()
    result = attr1 - attr_empty
    assert result.strength == 10
    assert result.defense == 20
    assert result.intellect == 30
    assert result.willpower == 40
    assert result.dexterity == 50
    assert result.accuracy == 60
    assert result.speed == 70
    assert result.luck == 80

    attr_float = AttributeModifier(1.2, 3.4, 5.6, 7.8, 9.1, 2.3, 4.5, 6.7, frac=True)
    with pytest.raises(ValueError):
        attr1 + attr_float

def test_attr_iadd():
    # Test in-place addition of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = AttributeModifier(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
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
    attr_empty = AttributeModifier()
    attr1 += attr_empty
    assert attr1.strength == 15
    assert attr1.defense == 30
    assert attr1.intellect == 45
    assert attr1.willpower == 60
    assert attr1.dexterity == 75
    assert attr1.accuracy == 90
    assert attr1.speed == 105
    assert attr1.luck == 120

    attr_float = AttributeModifier(1.2, 3.4, 5.6, 7.8, 9.1, 2.3, 4.5, 6.7, frac=True)
    with pytest.raises(ValueError):
        attr1 += attr_float

def test_attr_isub():
    # Test in-place subtraction of two attributes
    attr1 = Attribute(strength=10, defense=20, intellect=30, willpower=40, dexterity=50, accuracy=60, speed=70, luck=80)
    attr2 = AttributeModifier(strength=5, defense=10, intellect=15, willpower=20, dexterity=25, accuracy=30, speed=35, luck=40)
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
    attr_empty = AttributeModifier()
    attr1 -= attr_empty
    assert attr1.strength == 5
    assert attr1.defense == 10
    assert attr1.intellect == 15
    assert attr1.willpower == 20
    assert attr1.dexterity == 25
    assert attr1.accuracy == 30
    assert attr1.speed == 35
    assert attr1.luck == 40

    attr_float = AttributeModifier(1.2, 3.4, 5.6, 7.8, 9.1, 2.3, 4.5, 6.7, frac=True)
    with pytest.raises(ValueError):
        attr1 -= attr_float

def test_attr_mul():
    attr = Attribute(10, 10, 10, 10, 10, 10, 10, 10)

    # Normal multiplication
    mod = AttributeModifier(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, True)
    result = attr * mod
    assert result.strength == 11
    assert result.defense == 12
    assert result.intellect == 13
    assert result.willpower == 14
    assert result.dexterity == 15
    assert result.accuracy == 16
    assert result.speed == 17
    assert result.luck == 18

    # Negative multiplication
    mod = AttributeModifier(-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, True)
    result = attr * mod
    assert result.strength == 9
    assert result.defense == 8
    assert result.intellect == 7
    assert result.willpower == 6
    assert result.dexterity == 5
    assert result.accuracy == 4
    assert result.speed == 3
    assert result.luck == 2

    # Default values
    mod = AttributeModifier(frac=True)
    result = attr * mod
    assert result.strength == 10
    assert result.defense == 10
    assert result.intellect == 10
    assert result.willpower == 10
    assert result.dexterity == 10
    assert result.accuracy == 10
    assert result.speed == 10
    assert result.luck == 10

    # Invalid value
    with pytest.raises(TypeError):
        attr * "not an attribute"
    
    # Invalid mod type
    with pytest.raises(ValueError):
        attr * AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)

def test_attr_imul():
    attr = Attribute(10, 10, 10, 10, 10, 10, 10, 10)

    # Normal
    mod = AttributeModifier(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, True)
    attr *= mod
    assert attr.strength == 11
    assert attr.defense == 12
    assert attr.intellect == 13
    assert attr.willpower == 14
    assert attr.dexterity == 15
    assert attr.accuracy == 16
    assert attr.speed == 17
    assert attr.luck == 18

    # Negative
    attr = Attribute(10, 10, 10, 10, 10, 10, 10, 10)
    mod = AttributeModifier(-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, True)
    attr *= mod
    assert attr.strength == 9
    assert attr.defense == 8
    assert attr.intellect == 7
    assert attr.willpower == 6
    assert attr.dexterity == 5
    assert attr.accuracy == 4
    assert attr.speed == 3
    assert attr.luck == 2

    # Default values
    attr = Attribute(10, 10, 10, 10, 10, 10, 10, 10)
    mod = AttributeModifier(frac=True)
    attr *= mod
    assert attr.strength == 10
    assert attr.defense == 10
    assert attr.intellect == 10
    assert attr.willpower == 10
    assert attr.dexterity == 10
    assert attr.accuracy == 10
    assert attr.speed == 10
    assert attr.luck == 10

    # Invalid value
    with pytest.raises(TypeError):
        attr = Attribute(10, 10, 10, 10, 10, 10, 10, 10)
        attr *= "not an attribute"

    # Invalid mod type
    with pytest.raises(ValueError):
        attr = Attribute(10, 10, 10, 10, 10, 10, 10, 10)
        attr *= AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)


# AttributeModifier
def test_attr_mod_init():
    # Default init
    attr = AttributeModifier()
    assert attr.strength == 0
    assert attr.defense == 0
    assert attr.intellect == 0
    assert attr.willpower == 0
    assert attr.dexterity == 0
    assert attr.accuracy == 0
    assert attr.speed == 0
    assert attr.luck == 0

    # Integer mod init
    attr1 = AttributeModifier(1, -2, 3, -4, 5, -6, 7, -8)
    attr2 = AttributeModifier(strength=1, defense=-2, intellect=3, willpower=-4, dexterity=5, accuracy=-6, speed=7, luck=-8)
    assert attr1.strength == attr2.strength == 1
    assert attr1.defense == attr2.defense == -2
    assert attr1.intellect == attr2.intellect == 3
    assert attr1.willpower == attr2.willpower == -4
    assert attr1.dexterity == attr2.dexterity == 5
    assert attr1.accuracy == attr2.accuracy == -6
    assert attr1.speed == attr2.speed == 7
    assert attr1.luck == attr2.luck == -8
    assert attr1.isinteger and attr2.isinteger
    assert not (attr1.isfractional and attr2.isfractional)
    assert attr1.type == attr2.type == int

    # Float mod init
    attr1 = AttributeModifier(-1.5, 2.5, -3.5, 4.5, -5.5, 6.5, -7.5, 8.5, frac=True)
    attr2 = AttributeModifier(strength=-1.5, defense=2.5, intellect=-3.5, willpower=4.5, dexterity=-5.5, accuracy=6.5, speed=-7.5, luck=8.5, frac=True)
    assert attr1.strength == attr2.strength == -1.5
    assert attr1.defense == attr2.defense == 2.5
    assert attr1.intellect == attr2.intellect == -3.5
    assert attr1.willpower == attr2.willpower == 4.5
    assert attr1.dexterity == attr2.dexterity == -5.5
    assert attr1.accuracy == attr2.accuracy == 6.5
    assert attr1.speed == attr2.speed == -7.5
    assert attr1.luck == attr2.luck == 8.5
    assert attr1.isfractional and attr2.isfractional
    assert not (attr1.isinteger and attr2.isinteger)
    assert attr1.type == attr2.type == float

    # Conversion
    attr = AttributeModifier(1, 2.0, 3, 4.9, 5.1, -6.8, 7.2, 8, frac=False)
    assert attr.strength == 1
    assert attr.defense == 2
    assert attr.intellect == 3
    assert attr.willpower == 4
    assert attr.dexterity == 5
    assert attr.accuracy == -6
    assert attr.speed == 7
    assert attr.luck == 8
    assert attr.isinteger

    attr = AttributeModifier(1, 2.0, 3, 4.9, 5.1, -6.8, 7.2, 8, frac=True)
    assert attr.strength == 1.0
    assert attr.defense == 2.0
    assert attr.intellect == 3.0
    assert attr.willpower == 4.9
    assert attr.dexterity == 5.1
    assert attr.accuracy == -6.8
    assert attr.speed == 7.2
    assert attr.luck == 8.0
    assert attr.isfractional

    # Type checking
    with pytest.raises(TypeError):
        AttributeModifier("a", "b", "c", "d", "e", "f", "g", "h")
    
    with pytest.raises(TypeError):
        AttributeModifier(1, 2, 3.5, 4, 5, 6, 7, "8")


def test_attr_mod_str_rep():
    # Integer
    attr = AttributeModifier(1, -2, 3, 0, -5, 6, -7, 8)
    assert str(attr) == "STR/DEF/INT/WIL/DEX/ACC/SPD/LCK: (+1/-2/+3/+0/-5/+6/-7/+8)"
    assert repr(attr) == "Attribute(strength=1, defense=-2, intellect=3, willpower=0, dexterity=-5, accuracy=6, speed=-7, luck=8, frac=False)"

    # Float
    attr = AttributeModifier(-0.1, 0.2, -0.3, 0.0, 0.5, -0.6, 0.7, -0.8, frac=True)
    assert str(attr) == "STR/DEF/INT/WIL/DEX/ACC/SPD/LCK: (-10%/+20%/-30%/+0%/+50%/-60%/+70%/-80%)"
    assert repr(attr) == "Attribute(strength=-0.1, defense=0.2, intellect=-0.3, willpower=0.0, dexterity=0.5, accuracy=-0.6, speed=0.7, luck=-0.8, frac=True)"

def test_attr_mod_add():
    # Int addition
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) 
    mod = AttributeModifier(8, -7, -6, 5, 4, -3, -2, -1)
    result = base + mod

    assert result.strength == 9
    assert result.defense == -5
    assert result.intellect == -3
    assert result.willpower == 9
    assert result.dexterity == 9
    assert result.accuracy == 3
    assert result.speed == 5
    assert result.luck == 7

    # Float addition
    base = AttributeModifier(1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, frac=True)
    mod = AttributeModifier(8.1, -7.2, -6.3, 5.4, 4.5, -3.6, -2.7, -1.8, frac=True)
    result = base + mod

    assert result.strength == 10.0
    assert result.defense == -4.4
    assert result.intellect == -2.6
    assert result.willpower == 10.0
    assert result.dexterity == 10.0
    assert result.accuracy == 2.8
    assert result.speed == 4.6
    assert result.luck == 6.4

    # Addition with blank values
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    mod = AttributeModifier()
    result = base + mod
    assert result.strength == 1
    assert result.defense == 2
    assert result.intellect == 3
    assert result.willpower == 4
    assert result.dexterity == 5
    assert result.accuracy == 6
    assert result.speed == 7
    assert result.luck == 8

    base = AttributeModifier(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, frac=True)
    mod = AttributeModifier(frac=True)
    result = base + mod

    assert result.strength == 1.5
    assert result.defense == 2.5
    assert result.intellect == 3.5
    assert result.willpower == 4.5
    assert result.dexterity == 5.5
    assert result.accuracy == 6.5
    assert result.speed == 7.5
    assert result.luck == 8.5
    
    
    # Invalid operand
    with pytest.raises(TypeError):
        base + "not an attribute"

    # Conflicting types
    with pytest.raises(ValueError):
        AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True) + AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    with pytest.raises(ValueError):
        AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) + AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True)

def test_attr_mod_sub():
    # Int subtraction
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) 
    mod = AttributeModifier(8, -7, -6, 5, 4, -3, -2, -1)
    result = base - mod

    assert result.strength == -7
    assert result.defense == 9
    assert result.intellect == 9
    assert result.willpower == -1
    assert result.dexterity == 1
    assert result.accuracy == 9
    assert result.speed == 9
    assert result.luck == 9

    # Float subtraction
    base = AttributeModifier(1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, frac=True)
    mod = AttributeModifier(8.1, -7.2, -6.3, 5.4, 4.5, -3.6, -2.7, -1.8, frac=True)
    result = base - mod

    assert result.strength == -6.2
    assert result.defense == 10.0
    assert result.intellect == 10.0
    assert result.willpower == -0.8
    assert result.dexterity == 1.0
    assert result.accuracy == 10.0
    assert result.speed == 10.0
    assert result.luck == 10.0

    # Subtraction with blank values
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    mod = AttributeModifier()
    result = base - mod
    assert result.strength == 1
    assert result.defense == 2
    assert result.intellect == 3
    assert result.willpower == 4
    assert result.dexterity == 5
    assert result.accuracy == 6
    assert result.speed == 7
    assert result.luck == 8

    base = AttributeModifier(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, frac=True)
    mod = AttributeModifier(frac=True)
    result = base - mod

    assert result.strength == 1.5
    assert result.defense == 2.5
    assert result.intellect == 3.5
    assert result.willpower == 4.5
    assert result.dexterity == 5.5
    assert result.accuracy == 6.5
    assert result.speed == 7.5
    assert result.luck == 8.5
    
    # Invalid operand
    with pytest.raises(TypeError):
        base - "not an attribute"

    # Conflicting types
    with pytest.raises(ValueError):
        AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True) - AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    with pytest.raises(ValueError):
        AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) - AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True)

def test_attr_mod_iadd():
    # Int addition
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) 
    mod = AttributeModifier(8, -7, -6, 5, 4, -3, -2, -1)
    base += mod

    assert base.strength == 9
    assert base.defense == -5
    assert base.intellect == -3
    assert base.willpower == 9
    assert base.dexterity == 9
    assert base.accuracy == 3
    assert base.speed == 5
    assert base.luck == 7

    # Float addition
    base = AttributeModifier(1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, frac=True)
    mod = AttributeModifier(8.1, -7.2, -6.3, 5.4, 4.5, -3.6, -2.7, -1.8, frac=True)
    base += mod
    
    assert base.strength == 10.0
    assert base.defense == -4.4
    assert base.intellect == -2.6
    assert base.willpower == 10.0
    assert base.dexterity == 10.0
    assert base.accuracy == 2.8
    assert base.speed == 4.6
    assert base.luck == 6.4

    # Addition with blank values
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    mod = AttributeModifier()
    base += mod
    assert base.strength == 1
    assert base.defense == 2
    assert base.intellect == 3
    assert base.willpower == 4
    assert base.dexterity == 5
    assert base.accuracy == 6
    assert base.speed == 7
    assert base.luck == 8

    base = AttributeModifier(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, frac=True)
    mod = AttributeModifier(frac=True)
    base += mod

    assert base.strength == 1.5
    assert base.defense == 2.5
    assert base.intellect == 3.5
    assert base.willpower == 4.5
    assert base.dexterity == 5.5
    assert base.accuracy == 6.5
    assert base.speed == 7.5
    assert base.luck == 8.5
    
    
    # Invalid operand
    with pytest.raises(TypeError):
        base += "not an attribute"

    # Conflicting types
    with pytest.raises(ValueError):
        attr = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True) 
        attr += AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    with pytest.raises(ValueError):
        attr = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=False) 
        attr += AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True)


def test_attr_mod_isub():
    # Int subtraction
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) 
    mod = AttributeModifier(8, -7, -6, 5, 4, -3, -2, -1)
    base -= mod

    assert base.strength == -7
    assert base.defense == 9
    assert base.intellect == 9
    assert base.willpower == -1
    assert base.dexterity == 1
    assert base.accuracy == 9
    assert base.speed == 9
    assert base.luck == 9

    # Float subtraction
    base = AttributeModifier(1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, frac=True)
    mod = AttributeModifier(8.1, -7.2, -6.3, 5.4, 4.5, -3.6, -2.7, -1.8, frac=True)
    base -= mod

    assert base.strength == -6.2
    assert base.defense == 10.0
    assert base.intellect == 10.0
    assert base.willpower == -0.8
    assert base.dexterity == 1.0
    assert base.accuracy == 10.0
    assert base.speed == 10.0
    assert base.luck == 10.0

    # Subtraction with blank values
    base = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    mod = AttributeModifier()
    base -= mod
    assert base.strength == 1
    assert base.defense == 2
    assert base.intellect == 3
    assert base.willpower == 4
    assert base.dexterity == 5
    assert base.accuracy == 6
    assert base.speed == 7
    assert base.luck == 8

    base = AttributeModifier(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, frac=True)
    mod = AttributeModifier(frac=True)
    base -= mod

    assert base.strength == 1.5
    assert base.defense == 2.5
    assert base.intellect == 3.5
    assert base.willpower == 4.5
    assert base.dexterity == 5.5
    assert base.accuracy == 6.5
    assert base.speed == 7.5
    assert base.luck == 8.5
    
    # Invalid operand
    with pytest.raises(TypeError):
        base -= "not an attribute"

    # Conflicting types
    with pytest.raises(ValueError):
        attr = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True) 
        attr -= AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8)
    with pytest.raises(ValueError):
        attr = AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8) 
        attr -= AttributeModifier(1, 2, 3, 4, 5, 6, 7, 8, frac=True)
        



