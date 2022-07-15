from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    given a range, return a list of the odd or even integers in that range.

    :param start: first integer of range
    :param stop: last integer of range
    :param parity: if we want to return odds or evens
    :return: list of integers
    """
    if parity == parity.EVEN:
        even_list = [str(value) for value in range(start, stop) if value % 2 == 0]
        print(even_list)
    else:
        odd_list = [str(value) for value in range(start, stop) if value % 2 != 0]
        print(odd_list)


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    ####one example is squaring, the other is factorial. all within given range

    number = (strategy for x in range(start,stop))
    print(number)

    #pass


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    ###need to iterate through string and do a .lower to get the values given to lowercase

    pass
