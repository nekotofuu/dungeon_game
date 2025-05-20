import random

def randstr(
        length: int = 10,
        ) -> str:
        string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQUESTUVWXYZ ,./;'\\-=!@#$%^&*_+|\":?><`~1234567890"
        return "".join(random.choices(string, k=min(length, len(string))))

def randbool() -> bool:
        return bool(random.randint(0,1))