def numcheck(val_chk=True, type_chk=True):
    def decorator(func):
        def wrapper(self, other):
            if type_chk \
               and (not isinstance(other, (int, float)) \
               or type(other) == bool):
                raise TypeError(f"Expected int or float, got {type(other).__name__}")
            if val_chk and other < 0:
                raise ValueError(f"Expected non-negative value, got {other}")
            return func(self, other)
        return wrapper
    return decorator
