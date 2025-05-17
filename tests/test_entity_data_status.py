# type: ignore

import pytest
from classes.data.status import Status, StatusModifier

def test_int_status_mod_init():
    # All case
    s = StatusModifier(1, 2, 3, 4)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    # Default case
    s = StatusModifier()
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0


    # Type checking
    s = StatusModifier(1, 2, 3, 4, frac=False)
    assert not s.isfractional
    assert s.isinteger

    s = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=False)
    assert not s.isfractional
    assert s.isinteger

    s = StatusModifier(1, 2, 3, 4)
    assert not s.isfractional
    assert s.isinteger

    # Partial case
    s = StatusModifier(health=1)
    assert s.health == 1
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0

    s = StatusModifier(mana=2)
    assert s.health == 0
    assert s.mana == 2
    assert s.max_health == 0
    assert s.max_mana == 0

    s = StatusModifier(max_health=3)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 3
    assert s.max_mana == 0

    s = StatusModifier(max_mana=4)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 4

    # Conversion
    s = StatusModifier(1.2, 2.4, 9.0, 5.2)
    assert isinstance(s.health, int)
    assert isinstance(s.mana, int)
    assert isinstance(s.max_health, int)
    assert isinstance(s.max_mana, int)
    
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 9
    assert s.max_mana == 5

    # Negative handling
    s = StatusModifier(-1, -2, -3, -4)
    assert s.health == -1
    assert s.mana == -2
    assert s.max_health == -3
    assert s.max_mana == -4

    # Invalid handling
    with pytest.raises(TypeError):
        s = StatusModifier("health", "mana", "max_health", "max_mana")

def test_int_status_mod_setters():
    s = StatusModifier(1, 3, 9, 20)
    
    # Normal values
    s.health = 5
    s.mana = 10
    s.max_health = 15
    s.max_mana = 25

    assert s.health == 5
    assert s.mana == 10
    assert s.max_health == 15
    assert s.max_mana == 25

    # Float values
    s.health = 1.4
    s.mana = 9.9
    s.max_health = 3.14159
    s.max_mana = 2.71828

    assert isinstance(s.health, int)
    assert isinstance(s.mana, int)
    assert isinstance(s.max_health, int)
    assert isinstance(s.max_mana, int)

    assert s.health == 1
    assert s.mana == 9
    assert s.max_health == 3
    assert s.max_mana == 2

    # Negative values
    s.health = -1
    s.mana = -2
    s.max_health = -3
    s.max_mana = -4

    assert s.health == -1
    assert s.mana == -2
    assert s.max_health == -3
    assert s.max_mana == -4

    # Invalid values
    with pytest.raises(TypeError):
        s.health = "health"
    with pytest.raises(TypeError):
        s.mana = "mana"
    with pytest.raises(TypeError):
        s.max_health = True
    with pytest.raises(TypeError):
        s.max_mana = str


def test_float_status_mod_init():
   # All case
    s = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    assert s.health == 1.2
    assert s.mana == 2.4
    assert s.max_health == 3.6
    assert s.max_mana == 4.8
    assert s.isfractional
    assert not s.isinteger

    # Default case
    s = StatusModifier(frac=True)
    assert s.health == 0.0
    assert s.mana == 0.0
    assert s.max_health == 0.0
    assert s.max_mana == 0.0
    assert s.isfractional
    assert not s.isinteger

    # Type checking
    s = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    assert s.isfractional
    assert not s.isinteger

    s = StatusModifier(1, 2, 3, 4, frac=True)
    assert s.isfractional
    assert not s.isinteger

    # Partial case
    s = StatusModifier(health=1.2, frac=True)
    assert s.health == 1.2
    assert s.mana == 0.0
    assert s.max_health == 0.0
    assert s.max_mana == 0.0

    s = StatusModifier(mana=2.4, frac=True)
    assert s.health == 0.0
    assert s.mana == 2.4
    assert s.max_health == 0.0
    assert s.max_mana == 0.0

    s = StatusModifier(max_health=3.6, frac=True)
    assert s.health == 0.0
    assert s.mana == 0.0
    assert s.max_health == 3.6
    assert s.max_mana == 0.0

    s = StatusModifier(max_mana=4.8, frac=True)
    assert s.health == 0.0
    assert s.mana == 0.0
    assert s.max_health == 0.0
    assert s.max_mana == 4.8

    # Conversion
    s = StatusModifier(1, 2, 3, 4, frac=True)
    assert isinstance(s.health, float)
    assert isinstance(s.mana, float)
    assert isinstance(s.max_health, float)
    assert isinstance(s.max_mana, float)

    assert s.health == 1.0
    assert s.mana == 2.0
    assert s.max_health == 3.0
    assert s.max_mana == 4.0

    assert s.isfractional
    assert not s.isinteger

    # Negative handling
    s = StatusModifier(-1.2, -2.4, -3.6, -4.8, frac=True)
    assert s.health == -1.2
    assert s.mana == -2.4
    assert s.max_health == -3.6
    assert s.max_mana == -4.8
    assert s.isfractional
    assert not s.isinteger


    # Invalid handling
    with pytest.raises(TypeError):
        s = StatusModifier("health", "mana", "max_health", "max_mana", frac=True)

def test_float_status_mod_setters():
    # Normal values
    s = StatusModifier(1.2, 3.4, 5.6, 7.8, frac=True)
    s.health = 9.1
    s.mana = 2.3
    s.max_health = 4.5
    s.max_mana = 6.7

    assert s.health == 9.1
    assert s.mana == 2.3
    assert s.max_health == 4.5
    assert s.max_mana == 6.7

    # Int values
    s.health = 1
    s.mana = 2
    s.max_health = 3
    s.max_mana = 4

    assert isinstance(s.health, float)
    assert isinstance(s.mana, float)
    assert isinstance(s.max_health, float)
    assert isinstance(s.max_mana, float)

    assert s.health == 1.0
    assert s.mana == 2.0
    assert s.max_health == 3.0
    assert s.max_mana == 4.0

    # Negative values
    s.health = -1.2
    s.mana = -2.4
    s.max_health = -3.6
    s.max_mana = -4.8

    assert s.health == -1.2
    assert s.mana == -2.4
    assert s.max_health == -3.6
    assert s.max_mana == -4.8

    # Invalid values
    with pytest.raises(TypeError):
        s.health = "health"
    with pytest.raises(TypeError):
        s.mana = "mana"
    with pytest.raises(TypeError):
        s.max_health = True
    with pytest.raises(TypeError):
        s.max_mana = str

def test_status_modifiers_str_rep():
    s_float = StatusModifier(-0.5, 2, -3, 4, frac=True)
    s_int = StatusModifier(1, -2, 3, 0)

    assert repr(s_float) == "StatusModifier(health=-0.5, mana=2.0, max_health=-3.0, max_mana=4.0, frac=True)"
    assert repr(s_int) == "StatusModifier(health=1, mana=-2, max_health=3, max_mana=0, frac=False)"

    assert str(s_float) == "-50%/+200% (-300%/+400%)"
    assert str(s_int) == "+1/-2 (+3/+0)"


def test_status_modifiers_add():
    # Integer
    ## Normal
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(5, 6, 7, 8)
    s = s1 + s2
    assert s.health == 6
    assert s.mana == 8
    assert s.max_health == 10
    assert s.max_mana == 12

    ## Partial
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(health=1)
    s = s1 + s2
    assert s.health == 2
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    s2 = StatusModifier(mana=2)
    s = s1 + s2
    assert s.health == 1
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    s2 = StatusModifier(max_health=2)
    s = s1 + s2
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 5
    assert s.max_mana == 4

    s2 = StatusModifier(max_mana=2)
    s = s1 + s2
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 6

    ## Negative addition
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(-5, 6, 7, -8)
    s = s1 + s2
    assert s.health == -4
    assert s.mana == 8
    assert s.max_health == 10
    assert s.max_mana == -4

    # Fractional
    ## Normal
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(5.6, 7.8, 9.0, 10.1, frac=True)
    s = s1 + s2
    assert s.health == 6.8
    assert s.mana == 10.2
    assert s.max_health == 12.6
    assert s.max_mana == 14.9

    ## Partial
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(health=1.2, frac=True)
    s = s1 + s2
    assert s.health == 2.4
    assert s.mana == 2.4
    assert s.max_health == 3.6
    assert s.max_mana == 4.8

    s2 = StatusModifier(mana=2.4, frac=True)
    s = s1 + s2
    assert s.health == 1.2
    assert s.mana == 4.8
    assert s.max_health == 3.6
    assert s.max_mana == 4.8

    s2 = StatusModifier(max_health=2.4, frac=True)
    s = s1 + s2
    assert s.health == 1.2
    assert s.mana == 2.4
    assert s.max_health == 6.0
    assert s.max_mana == 4.8

    s2 = StatusModifier(max_mana=2.4, frac=True)
    s = s1 + s2
    assert s.health == 1.2
    assert s.mana == 2.4
    assert s.max_health == 3.6
    assert s.max_mana == 7.2

    ## Negative addition
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(-5.6, 7.8, 9.0, -10.1, frac=True)
    s = s1 + s2
    assert s.health == -4.4
    assert s.mana == 10.2
    assert s.max_health == 12.6
    assert s.max_mana == -5.3

    # Invalid operand
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s = s1 + s2

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s = s1 + s2
    
    # Invalid type
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    with pytest.raises(ValueError):
        s = s1 + s2

    # Invalid type
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(1, 2, 3, 4)
    with pytest.raises(ValueError):
        s = s1 + s2
    

def test_status_modifiers_iadd():
    # Integer
    ## Normal
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(5, 6, 7, 8)
    s1 += s2
    assert s1.health == 6
    assert s1.mana == 8
    assert s1.max_health == 10
    assert s1.max_mana == 12
    
    ## Partial
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(health=1)
    s1 += s2
    assert s1.health == 2
    assert s1.mana == 2
    assert s1.max_health == 3
    assert s1.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(mana=2)
    s1 += s2
    assert s1.health == 1
    assert s1.mana == 4
    assert s1.max_health == 3
    assert s1.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(max_health=2)
    s1 += s2
    assert s1.health == 1
    assert s1.mana == 2
    assert s1.max_health == 5
    assert s1.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(max_mana=2)
    s1 += s2
    assert s1.health == 1
    assert s1.mana == 2
    assert s1.max_health == 3
    assert s1.max_mana == 6
    
    ## Negative addition
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(-5, 6, 7, -8)
    s1 += s2
    assert s1.health == -4
    assert s1.mana == 8
    assert s1.max_health == 10
    assert s1.max_mana == -4

    # Fractional
    ## Normal
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(5.6, 7.8, 9.0, 10.1, frac=True)
    s1 += s2
    assert s1.health == 6.8
    assert s1.mana == 10.2
    assert s1.max_health == 12.6
    assert s1.max_mana == 14.9

    ## Partial
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(health=1.2, frac=True)
    s1 += s2
    assert s1.health == 2.4
    assert s1.mana == 2.4
    assert s1.max_health == 3.6
    assert s1.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(mana=2.4, frac=True)
    s1 += s2
    assert s1.health == 1.2
    assert s1.mana == 4.8
    assert s1.max_health == 3.6
    assert s1.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(max_health=2.4, frac=True)
    s1 += s2
    assert s1.health == 1.2
    assert s1.mana == 2.4
    assert s1.max_health == 6.0
    assert s1.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(max_mana=2.4, frac=True)
    s1 += s2
    assert s1.health == 1.2
    assert s1.mana == 2.4
    assert s1.max_health == 3.6
    assert s1.max_mana == 7.2

    ## Negative addition
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(-5.6, 7.8, 9.0, -10.1, frac=True)
    s1 += s2
    assert s1.health == -4.4
    assert s1.mana == 10.2
    assert s1.max_health == 12.6
    assert s1.max_mana == -5.3

    # Invalid operand
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s1 += s2
    
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s1 += s2

    # Invalid type
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    with pytest.raises(ValueError):
        s1 += s2

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(1, 2, 3, 4)
    with pytest.raises(ValueError):
        s1 += s2

def test_status_modifiers_sub():
    # Integer
    ## Normal
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(5, 6, 7, 8)
    s = s1 - s2
    assert s.health == -4
    assert s.mana == -4
    assert s.max_health == -4
    assert s.max_mana == -4

    ## Partial
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(health=1)
    s = s1 - s2
    assert s.health == 0
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(mana=2)
    s = s1 - s2
    assert s.health == 1
    assert s.mana == 0
    assert s.max_health == 3
    assert s.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(max_health=2)
    s = s1 - s2
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 1
    assert s.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(max_mana=2)
    s = s1 - s2
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 2

    ## Negative subtraction
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(-5, 6, 7, -8)
    s = s1 - s2
    assert s.health == 6
    assert s.mana == -4
    assert s.max_health == -4
    assert s.max_mana == 12

    # Fractional
    ## Normal
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(5.6, 7.8, 9.0, 10.1, frac=True)
    s = s1 - s2
    assert s.health == -4.4
    assert s.mana == -5.4
    assert s.max_health == -5.4
    assert s.max_mana == -5.3

    ## Partial
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(health=1.2, frac=True)
    s = s1 - s2
    assert s.health == 0.0
    assert s.mana == 2.4
    assert s.max_health == 3.6
    assert s.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(mana=2.4, frac=True)
    s = s1 - s2
    assert s.health == 1.2
    assert s.mana == 0.0
    assert s.max_health == 3.6
    assert s.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(max_health=2.4, frac=True)
    s = s1 - s2
    assert s.health == 1.2
    assert s.mana == 2.4
    assert s.max_health == 1.2
    assert s.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(max_mana=2.4, frac=True)
    s = s1 - s2
    assert s.health == 1.2
    assert s.mana == 2.4
    assert s.max_health == 3.6
    assert s.max_mana == 2.4

    ## Negative subtraction
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(-5.6, 7.8, 9.0, -10.1, frac=True)
    s = s1 - s2
    assert s.health == 6.8
    assert s.mana == -5.4
    assert s.max_health == -5.4
    assert s.max_mana == 14.9

    # Invalid operand
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s = s1 - s2

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s = s1 - s2

    # Invalid type
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    with pytest.raises(ValueError):
        s = s1 - s2

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(1, 2, 3, 4)
    with pytest.raises(ValueError):
        s = s1 - s2


def test_status_modifiers_isub():
    # Integer
    ## Normal
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(5, 6, 7, 8)
    s1 -= s2
    assert s1.health == -4
    assert s1.mana == -4
    assert s1.max_health == -4
    assert s1.max_mana == -4

    ## Partial
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(health=1)
    s1 -= s2
    assert s1.health == 0
    assert s1.mana == 2
    assert s1.max_health == 3
    assert s1.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(mana=2)
    s1 -= s2
    assert s1.health == 1
    assert s1.mana == 0
    assert s1.max_health == 3
    assert s1.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(max_health=2)
    s1 -= s2
    assert s1.health == 1
    assert s1.mana == 2
    assert s1.max_health == 1
    assert s1.max_mana == 4

    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(max_mana=2)
    s1 -= s2
    assert s1.health == 1
    assert s1.mana == 2
    assert s1.max_health == 3
    assert s1.max_mana == 2

    ## Negative subtraction
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(-5, 6, 7, -8)
    s1 -= s2
    assert s1.health == 6
    assert s1.mana == -4
    assert s1.max_health == -4
    assert s1.max_mana == 12

    # Fractional
    ## Normal
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(5.6, 7.8, 9.0, 10.1, frac=True)
    s1 -= s2
    assert s1.health == -4.4
    assert s1.mana == -5.4
    assert s1.max_health == -5.4
    assert s1.max_mana == -5.3

    ## Partial
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(health=1.2, frac=True)
    s1 -= s2
    assert s1.health == 0.0
    assert s1.mana == 2.4
    assert s1.max_health == 3.6
    assert s1.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(mana=2.4, frac=True)
    s1 -= s2
    assert s1.health == 1.2
    assert s1.mana == 0.0
    assert s1.max_health == 3.6
    assert s1.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(max_health=2.4, frac=True)
    s1 -= s2
    assert s1.health == 1.2
    assert s1.mana == 2.4
    assert s1.max_health == 1.2
    assert s1.max_mana == 4.8

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(max_mana=2.4, frac=True)
    s1 -= s2
    assert s1.health == 1.2
    assert s1.mana == 2.4
    assert s1.max_health == 3.6
    assert s1.max_mana == 2.4
    
    ## Negative subtraction
    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(-5.6, 7.8, 9.0, -10.1, frac=True)
    s1 -= s2
    assert s1.health == 6.8
    assert s1.mana == -5.4
    assert s1.max_health == -5.4
    assert s1.max_mana == 14.9

    # Invalid operand
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s1 -= s2

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s1 -= s2

    # Invalid type
    s1 = StatusModifier(1, 2, 3, 4)
    s2 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    with pytest.raises(ValueError):
        s1 -= s2

    s1 = StatusModifier(1.2, 2.4, 3.6, 4.8, frac=True)
    s2 = StatusModifier(1, 2, 3, 4)
    with pytest.raises(ValueError):
        s1 -= s2

def test_status_init():
    # Default case
    s = Status()
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0
    assert isinstance(s.health, int)
    assert isinstance(s.mana, int)
    assert isinstance(s.max_health, int)
    assert isinstance(s.max_mana, int)
    
    # Normal case
    s = Status(1, 2, 3, 4)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    # Current value overflow
    s = Status(4, 3, 2, 1)
    assert s.health == 2
    assert s.mana == 1
    assert s.max_health == 2
    assert s.max_mana == 1

    # Partial case
    s = Status(health=1)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0

    s = Status(mana=2)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0

    s = Status(max_health=3)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 3
    assert s.max_mana == 0

    s = Status(max_mana=4)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 4


    # Float value handling
    s = Status(0.1, 5.2, 9.3, 7.4)
    assert isinstance(s.health, int)
    assert isinstance(s.mana, int)
    assert isinstance(s.max_health, int)
    assert isinstance(s.max_mana, int)

    assert s.health == 0
    assert s.mana == 5
    assert s.max_health == 9
    assert s.max_mana == 7

    # Negative value handling
    with pytest.raises(ValueError):
        s = Status(-1, -2, -3, -4)

    # Invalid type handling
    with pytest.raises(TypeError):
        s = Status("health", "mana", "max_health", "max_mana")

def test_status_str_rep():
    s = Status(1, 2, 3, 4)
    assert repr(s) == "Status(health=1, mana=2, max_health=3, max_mana=4)"
    assert str(s) == "1/2 (3/4)"

def test_status_setters():
    s = Status(1, 2, 3, 4)

    # Normal values
    s.health = 5
    s.mana = 6
    s.max_health = 7
    s.max_mana = 8

    assert s.health == 3
    assert s.mana == 4
    assert s.max_health == 7
    assert s.max_mana == 8

    # Overflow values
    s.health = 9
    s.mana = 10
    
    assert s.health == 7
    assert s.mana == 8
    assert s.max_health == 7
    assert s.max_mana == 8

    # Underflow values
    s.max_health = 6
    s.max_mana = 5

    assert s.health == 6
    assert s.mana == 5
    assert s.max_health == 6
    assert s.max_mana == 5

    # Type conversion
    s.health = 1.61
    s.mana = 2.71
    s.max_health = 6.28
    s.max_mana = 3.14
    
    assert isinstance(s.health, int)
    assert isinstance(s.mana, int)
    assert isinstance(s.max_health, int)
    assert isinstance(s.max_mana, int)

    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 6
    assert s.max_mana == 3

    # Negative values
    with pytest.raises(ValueError):
        s.health = -1
    with pytest.raises(ValueError):
        s.mana = -2
    with pytest.raises(ValueError):
        s.max_health = -3  
    with pytest.raises(ValueError):
        s.max_mana = -4

    # Invalid type
    with pytest.raises(TypeError):
        s.health = "health"
    with pytest.raises(TypeError):
        s.mana = {}
    with pytest.raises(TypeError):
        s.max_health = []
    with pytest.raises(TypeError):
        s.max_mana = True

def test_status_add():
    base = Status(1, 2, 3, 4)
    
    # Normal 
    modifier = StatusModifier(1, 2, 3, 4)
    s = base + modifier
    assert s.health == 2
    assert s.mana == 4
    assert s.max_health == 6
    assert s.max_mana == 8

    # Overflow
    modifier = StatusModifier(4, 4)
    s = base + modifier
    assert s.health == 3
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    # Partial
    modifier = StatusModifier(health=2)
    s = base + modifier
    assert s.health == 3
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    modifier = StatusModifier(mana=2)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    modifier = StatusModifier(max_health=2)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 5
    assert s.max_mana == 4

    modifier = StatusModifier(max_mana=2)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 6

    # Partial-overflow
    modifier = StatusModifier(health=4)
    s = base + modifier
    assert s.health == 3
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    modifier = StatusModifier(mana=4)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    # Negative addition
    modifier = StatusModifier(-1, -1, -1, -1)
    s = base + modifier
    assert s.health == 0
    assert s.mana == 1
    assert s.max_health == 2
    assert s.max_mana == 3

    # Negative addition-overflow
    with pytest.raises(ValueError):
        modifier = StatusModifier(health=-10)
        s = base + modifier
    with pytest.raises(ValueError):
        modifier = StatusModifier(mana=-10)
        s = base + modifier
    with pytest.raises(ValueError):
        modifier = StatusModifier(max_health=-10)
        s = base + modifier
    with pytest.raises(ValueError):
        modifier = StatusModifier(max_mana=-10)
        s = base + modifier
    
    # Invalid operand
    mod = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s = base + mod

    mod = StatusModifier(2.5, 3.5, 4.5, 5.5, frac=True)
    with pytest.raises(ValueError):
        s = base + mod

def test_status_iadd():
    s = Status(1, 2, 3, 4)
    
    # Normal
    s += StatusModifier(1, 2, 3, 4)
    assert s.health == 2
    assert s.mana == 4
    assert s.max_health == 6
    assert s.max_mana == 8

    # Overflow
    s += StatusModifier(8, 8)
    assert s.health == 6
    assert s.mana == 8
    assert s.max_health == 6
    assert s.max_mana == 8

    s = Status(1, 2, 3, 4)

    # Partial
    s += StatusModifier(health=1)
    assert s.health == 2
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    s += StatusModifier(mana=1)
    assert s.health == 2
    assert s.mana == 3
    assert s.max_health == 3
    assert s.max_mana == 4

    s += StatusModifier(max_health=1)
    assert s.health == 2
    assert s.mana == 3
    assert s.max_health == 4
    assert s.max_mana == 4

    s += StatusModifier(max_mana=1)
    assert s.health == 2
    assert s.mana == 3
    assert s.max_health == 4
    assert s.max_mana == 5

    # Negative addition
    s += StatusModifier(-1, -1, -1, -1)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    # Negative addition-overflow
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += StatusModifier(health=-10)
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += StatusModifier(mana=-10)
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += StatusModifier(max_health=-10)
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += StatusModifier(max_mana=-10)
    
    # Invalid operand
    with pytest.raises(TypeError):
        s = Status(1, 2, 3, 4)
        s += ["Invalid",  {"operand": 1}]
    
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += StatusModifier(2.5, 3.5, 4.5, 5.5, frac=True)

def test_status_sub():
    base = Status(10, 10, 10, 10)

    # Normal
    modifier = StatusModifier(4, 3, 2, 1)
    s = base - modifier
    assert s.health == 6
    assert s.mana == 7
    assert s.max_health == 8
    assert s.max_mana == 9

    # Partial
    modifier = StatusModifier(9, 8)
    s = base - modifier
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 10
    assert s.max_mana == 10

    # Overflow
    modifier = StatusModifier(max_health=5, max_mana=7)
    s = base - modifier
    assert s.health == 5
    assert s.mana == 3
    assert s.max_health == 5
    assert s.max_mana == 3

    # Partial specific
    modifier = StatusModifier(health=5)
    s = base - modifier
    assert s.health == 5
    assert s.mana == 10
    assert s.max_health == 10
    assert s.max_mana == 10 

    modifier = StatusModifier(mana=7)
    s = base - modifier
    assert s.health == 10
    assert s.mana == 3
    assert s.max_health == 10
    assert s.max_mana == 10

    # Negative Subraction
    modifier = StatusModifier(-1, -2, -3, -4)
    s = base - modifier
    assert s.health == 11
    assert s.mana == 12
    assert s.max_health == 13
    assert s.max_mana == 14

    # Negative subtraction-overflow
    modifier = StatusModifier(health=-10, mana=-10)
    s = base - modifier
    assert s.health == 10
    assert s.mana == 10
    assert s.max_health == 10
    assert s.max_mana == 10

    # Subtraction overflow
    with pytest.raises(ValueError):
        modifier = StatusModifier(100, 100, 100, 100)
        s = base - modifier

    # Invalid operand
    with pytest.raises(TypeError):
        s = base - ["Invalid",  {"operand": 1}]

    with pytest.raises(ValueError):
        s = base - StatusModifier(2.5, 3.5, 4.5, 5.5, frac=True)

def test_status_isub():
    s = Status(10, 10, 10, 10)

    # Normal
    s -= StatusModifier(1, 3, 2, 1)
    assert s.health == 7
    assert s.mana == 6
    assert s.max_health == 8
    assert s.max_mana == 9

    # Partial
    s -= StatusModifier(2, 1)
    assert s.health == 5
    assert s.mana == 5
    assert s.max_health == 8
    assert s.max_mana == 9

    # Overflow
    s -= StatusModifier(max_health=5, max_mana=7)
    assert s.health == 3
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 2

    # Partial specific
    s -= StatusModifier(health=2)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 2

    s -= StatusModifier(mana=2)
    assert s.health == 1
    assert s.mana == 0
    assert s.max_health == 3
    assert s.max_mana == 2

    # Negative Subtraction
    s -= StatusModifier(-1, -2, -3, -4)
    assert s.health == 2
    assert s.mana == 2
    assert s.max_health == 6
    assert s.max_mana == 6

    # Negative subtraction-overflow
    s -= StatusModifier(health=-10, mana=-10)
    assert s.health == 6
    assert s.mana == 6
    assert s.max_health == 6
    assert s.max_mana == 6

    # Subtraction overflow
    with pytest.raises(ValueError):
        s -= StatusModifier(100, 100, 100, 100)

    # Invalid operand
    with pytest.raises(TypeError):
        s -= ["Invalid",  {"operand": 1}]

    with pytest.raises(ValueError):
        s -= StatusModifier(2.5, 3.5, 4.5, 5.5, frac=True)
    
def test_status_mul():
    base = Status(10, 10, 100, 100)

    # Normal
    modifier = StatusModifier(0.5, 0.1, frac=True)
    s = base * modifier
    assert s.health == 60
    assert s.mana == 20
    assert s.max_health == 100
    assert s.max_mana == 100

    modifier = StatusModifier(max_health=0.2, max_mana=0.5, frac=True)
    s = base * modifier
    assert s.health == 10
    assert s.mana == 10
    assert s.max_health == 120
    assert s.max_mana == 150

    # Overflow
    modifier = StatusModifier(2, 5, frac=True)
    s = base * modifier
    assert s.health == 100
    assert s.mana == 100
    assert s.max_health == 100
    assert s.max_mana == 100

    # Negative multiplication
    modifier = StatusModifier(-0.01, -0.05, frac=True)
    s = base * modifier
    assert s.health == 9
    assert s.mana == 5
    assert s.max_health == 100
    assert s.max_mana == 100

    # Negative multiplication overflow
    with pytest.raises(ValueError):
        modifier = StatusModifier(-2.0, -3.0, frac=True)
        s = base * modifier
    
    # Invalid operand
    with pytest.raises(TypeError):
        s = base * "invalid"

    with pytest.raises(ValueError):
        s = base * StatusModifier(2, 3, 4, 5)

def test_status_imul():
    s = Status(10, 10, 100, 100)

    # Normal
    s *= StatusModifier(0.5, 0.1, frac=True)
    assert s.health == 60
    assert s.mana == 20
    assert s.max_health == 100
    assert s.max_mana == 100

    # Partial
    s = Status(10, 10, 100, 100)

    s *= StatusModifier(health=0.2, frac=True)
    assert s.health == 30
    assert s.mana == 10
    assert s.max_health == 100
    assert s.max_mana == 100

    s = Status(10, 10, 100, 100)
    s *= StatusModifier(mana=0.75, frac=True)
    assert s.health == 10
    assert s.mana == 85
    assert s.max_health == 100
    assert s.max_mana == 100

    # Overflow
    s = Status(30, 80, 100, 100)
    s *= StatusModifier(0.8, 0.3, frac=True)
    assert s.health == 100
    assert s.mana == 100
    assert s.max_health == 100
    assert s.max_mana == 100

    # Negative multiplication
    s = Status(100, 100, 100, 100)
    s *= StatusModifier(-0.5, -0.2, frac=True)    
    assert s.health == 50
    assert s.mana == 80
    assert s.max_health == 100
    assert s.max_mana == 100

    # Negative multiplication overflow
    with pytest.raises(ValueError):
        s = Status(100, 100, 100, 100)
        s *= StatusModifier(-2.0, -3.0, frac=True)

    # Invalid operand
    with pytest.raises(TypeError):
        s = Status(10, 10, 100, 100)
        s *= "invalid"

    with pytest.raises(ValueError):
        s = Status(10, 10, 100, 100)
        s *= StatusModifier(2, 3, 4, 5)