# type: ignore

import pytest
from classes.data.status import Status, IntStatusModifier, FloatStatusModifier

def test_int_status_mod_init():
    # All case
    s = IntStatusModifier(1, 2, 3, 4)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    # Default case
    s = IntStatusModifier()
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0

    # Partial case
    s = IntStatusModifier(_health=1)
    assert s.health == 1
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 0

    s = IntStatusModifier(_mana=2)
    assert s.health == 0
    assert s.mana == 2
    assert s.max_health == 0
    assert s.max_mana == 0

    s = IntStatusModifier(_max_health=3)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 3
    assert s.max_mana == 0

    s = IntStatusModifier(_max_mana=4)
    assert s.health == 0
    assert s.mana == 0
    assert s.max_health == 0
    assert s.max_mana == 4

    # Conversion
    s = IntStatusModifier(1.2, 2.4, 9.0, 5.2)
    assert isinstance(s.health, int)
    assert isinstance(s.mana, int)
    assert isinstance(s.max_health, int)
    assert isinstance(s.max_mana, int)
    
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 9
    assert s.max_mana == 5

    # Negative handling
    s = IntStatusModifier(-1, -2, -3, -4)
    assert s.health == -1
    assert s.mana == -2
    assert s.max_health == -3
    assert s.max_mana == -4

    # Invalid handling
    with pytest.raises(TypeError):
        s = IntStatusModifier("health", "mana", "max_health", "max_mana")

def test_int_status_mod_setters():
    s = IntStatusModifier(1, 3, 9, 20)
    
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
    # Normal case
    s = FloatStatusModifier(0.1, 0.2)
    assert s.health == 0.1
    assert s.mana == 0.2

    # Default case
    s = FloatStatusModifier()
    assert s.health == 0.0
    assert s.mana == 0.0

    # Partial case
    s = FloatStatusModifier(_health=0.5)
    assert s.health == 0.5
    assert s.mana == 0.0

    s = FloatStatusModifier(_mana=0.3)
    assert s.health == 0.0
    assert s.mana == 0.3

    # Negative handling
    s = FloatStatusModifier(-0.79, -0.21)
    assert s.health == -0.79
    assert s.mana == -0.21

    # Conversion
    s = FloatStatusModifier(20, 50)
    assert isinstance(s.health, float)
    assert isinstance(s.mana, float)
    
    assert s.health == 20.0
    assert s.mana == 50.0

    # Invalid values
    with pytest.raises(TypeError):
        s = FloatStatusModifier("health", "mana")
    
def test_float_status_mod_setters():
    # Normal values
    s = FloatStatusModifier(0.1, 0.2)
    s.health = 0.5
    s.mana = 0.3

    assert s.health == 0.5
    assert s.mana == 0.3

    # Negative values
    s.health = -0.3012
    s.mana = -0.0001

    assert s.health == -0.3012
    assert s.mana == -0.0001

    # Int values
    s.health = 9
    s.mana = 5

    assert isinstance(s.health, float)
    assert isinstance(s.mana, float)
    assert s.health == 9.0
    assert s.mana == 5.0

    # Invalid values
    with pytest.raises(TypeError):
        s.health = []
    with pytest.raises(TypeError):
        s.mana = {}

def test_status_init():
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
    modifier = IntStatusModifier(1, 2, 3, 4)
    s = base + modifier
    assert s.health == 2
    assert s.mana == 4
    assert s.max_health == 6
    assert s.max_mana == 8

    # Overflow
    modifier = IntStatusModifier(4, 4)
    s = base + modifier
    assert s.health == 3
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    # Partial
    modifier = IntStatusModifier(_health=2)
    s = base + modifier
    assert s.health == 3
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    modifier = IntStatusModifier(_mana=2)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    modifier = IntStatusModifier(_max_health=2)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 5
    assert s.max_mana == 4

    modifier = IntStatusModifier(_max_mana=2)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 6

    # Partial-overflow
    modifier = IntStatusModifier(_health=4)
    s = base + modifier
    assert s.health == 3
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    modifier = IntStatusModifier(_mana=4)
    s = base + modifier
    assert s.health == 1
    assert s.mana == 4
    assert s.max_health == 3
    assert s.max_mana == 4

    # Negative addition
    modifier = IntStatusModifier(-1, -1, -1, -1)
    s = base + modifier
    assert s.health == 0
    assert s.mana == 1
    assert s.max_health == 2
    assert s.max_mana == 3

    # Negative addition-overflow
    with pytest.raises(ValueError):
        modifier = IntStatusModifier(_health=-10)
        s = base + modifier
    with pytest.raises(ValueError):
        modifier = IntStatusModifier(_mana=-10)
        s = base + modifier
    with pytest.raises(ValueError):
        modifier = IntStatusModifier(_max_health=-10)
        s = base + modifier
    with pytest.raises(ValueError):
        modifier = IntStatusModifier(_max_mana=-10)
        s = base + modifier
    
    # Invalid operand
    mod = ["Invalid",  {"operand": 1}]
    with pytest.raises(TypeError):
        s = base + mod

def test_status_iadd():
    s = Status(1, 2, 3, 4)
    
    # Normal
    s += IntStatusModifier(1, 2, 3, 4)
    assert s.health == 2
    assert s.mana == 4
    assert s.max_health == 6
    assert s.max_mana == 8

    # Overflow
    s += IntStatusModifier(8, 8)
    assert s.health == 6
    assert s.mana == 8
    assert s.max_health == 6
    assert s.max_mana == 8

    s = Status(1, 2, 3, 4)

    # Partial
    s += IntStatusModifier(_health=1)
    assert s.health == 2
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    s += IntStatusModifier(_mana=1)
    assert s.health == 2
    assert s.mana == 3
    assert s.max_health == 3
    assert s.max_mana == 4

    s += IntStatusModifier(_max_health=1)
    assert s.health == 2
    assert s.mana == 3
    assert s.max_health == 4
    assert s.max_mana == 4

    s += IntStatusModifier(_max_mana=1)
    assert s.health == 2
    assert s.mana == 3
    assert s.max_health == 4
    assert s.max_mana == 5

    # Negative addition
    s += IntStatusModifier(-1, -1, -1, -1)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 4

    # Negative addition-overflow
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += IntStatusModifier(_health=-10)
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += IntStatusModifier(_mana=-10)
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += IntStatusModifier(_max_health=-10)
    with pytest.raises(ValueError):
        s = Status(1, 2, 3, 4)
        s += IntStatusModifier(_max_mana=-10)
    
    # Invalid operand
    with pytest.raises(TypeError):
        s = Status(1, 2, 3, 4)
        s += ["Invalid",  {"operand": 1}]

def test_status_sub():
    base = Status(10, 10, 10, 10)

    # Normal
    modifier = IntStatusModifier(4, 3, 2, 1)
    s = base - modifier
    assert s.health == 6
    assert s.mana == 7
    assert s.max_health == 8
    assert s.max_mana == 9

    # Partial
    modifier = IntStatusModifier(9, 8)
    s = base - modifier
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 10
    assert s.max_mana == 10

    # Overflow
    modifier = IntStatusModifier(_max_health=5, _max_mana=7)
    s = base - modifier
    assert s.health == 5
    assert s.mana == 3
    assert s.max_health == 5
    assert s.max_mana == 3

    # Partial specific
    modifier = IntStatusModifier(_health=5)
    s = base - modifier
    assert s.health == 5
    assert s.mana == 10
    assert s.max_health == 10
    assert s.max_mana == 10 

    modifier = IntStatusModifier(_mana=7)
    s = base - modifier
    assert s.health == 10
    assert s.mana == 3
    assert s.max_health == 10
    assert s.max_mana == 10

    # Negative Subraction
    modifier = IntStatusModifier(-1, -2, -3, -4)
    s = base - modifier
    assert s.health == 11
    assert s.mana == 12
    assert s.max_health == 13
    assert s.max_mana == 14

    # Negative subtraction-overflow
    modifier = IntStatusModifier(_health=-10, _mana=-10)
    s = base - modifier
    assert s.health == 10
    assert s.mana == 10
    assert s.max_health == 10
    assert s.max_mana == 10

    # Subtraction overflow
    with pytest.raises(ValueError):
        modifier = IntStatusModifier(100, 100, 100, 100)
        s = base - modifier

    # Invalid operand
    with pytest.raises(TypeError):
        s = base - ["Invalid",  {"operand": 1}]

def test_status_isub():
    s = Status(10, 10, 10, 10)

    # Normal
    s -= IntStatusModifier(4, 3, 2, 1)
    assert s.health == 6
    assert s.mana == 7
    assert s.max_health == 8
    assert s.max_mana == 9

    # Partial
    s -= IntStatusModifier(1, 2)
    assert s.health == 5
    assert s.mana == 5
    assert s.max_health == 8
    assert s.max_mana == 9

    # Overflow
    s -= IntStatusModifier(_max_health=5, _max_mana=7)
    assert s.health == 3
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 2

    # Partial specific
    s -= IntStatusModifier(_health=2)
    assert s.health == 1
    assert s.mana == 2
    assert s.max_health == 3
    assert s.max_mana == 2

    s -= IntStatusModifier(_mana=2)
    assert s.health == 1
    assert s.mana == 0
    assert s.max_health == 3
    assert s.max_mana == 2

    # Negative Subtraction
    s -= IntStatusModifier(-1, -2, -3, -4)
    assert s.health == 2
    assert s.mana == 2
    assert s.max_health == 6
    assert s.max_mana == 6

    # Negative subtraction-overflow
    s -= IntStatusModifier(_health=-10, _mana=-10)
    assert s.health == 6
    assert s.mana == 6
    assert s.max_health == 6
    assert s.max_mana == 6

    # Subtraction overflow
    with pytest.raises(ValueError):
        s -= IntStatusModifier(100, 100, 100, 100)

    # Invalid operand
    with pytest.raises(TypeError):
        s -= ["Invalid",  {"operand": 1}]
    
def test_status_imult():
    s = Status(10, 10, 100, 100)

    # Normal
    s *= FloatStatusModifier(0.5, 0.1)
    assert s.health == 60
    assert s.mana == 20
    assert s.max_health == 100
    assert s.max_mana == 100

    # Partial
    s = Status(10, 10, 100, 100)

    s *= FloatStatusModifier(_health=0.2)
    assert s.health == 30
    assert s.mana == 10
    assert s.max_health == 100
    assert s.max_mana == 100

    s = Status(10, 10, 100, 100)
    s *= FloatStatusModifier(_mana=0.75)
    assert s.health == 10
    assert s.mana == 85
    assert s.max_health == 100
    assert s.max_mana == 100

    # Overflow
    s = Status(30, 80, 100, 100)
    s *= FloatStatusModifier(0.8, 0.3)
    assert s.health == 100
    assert s.mana == 100
    assert s.max_health == 100
    assert s.max_mana == 100

    # Negative multiplication
    s = Status(100, 100, 100, 100)
    s *= FloatStatusModifier(-0.5, -0.2)    
    assert s.health == 50
    assert s.mana == 80
    assert s.max_health == 100
    assert s.max_mana == 100

    # Negative multiplication overflow
    with pytest.raises(ValueError):
        s = Status(100, 100, 100, 100)
        s *= FloatStatusModifier(-2.0, -3.0)

    # Invalid operand
    with pytest.raises(TypeError):
        s = Status(10, 10, 100, 100)
        s *= "invalid"
    with pytest.raises(TypeError):
        s = Status(10, 10, 100, 100)
        s *= IntStatusModifier(1, 2, 3, 4)


