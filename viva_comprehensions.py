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

    # if parity == parity.EVEN:
    #     even_list = [str(value) for value in range(start, stop) if value % 2 == 0]
    #     print(even_list)
    # else:
    #     odd_list = [str(value) for value in range(start, stop) if value % 2 != 0]
    #     print(odd_list)

    return [num for num in range(start,stop) if (parity == parity.EVEN and num % 2 == 0)
            or (parity == parity.ODD and num % 2 != 0)]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    return a new dict by iterating through the range(start/stop integer) and applying a math formula


    :param start: starting integer
    :param stop: stopping integer
    :param strategy: math formulat (square, factorial)
    :return:
    """
    ####one example is squaring, the other is factorial. all within given range

    return {num: strategy(num) for num in range(start,stop)}

    #pass


def gen_set(val_in: str) -> Set:
    """
    return letters as uppercase

    :param val_in: string
    :return:
    """
    ###need to iterate through string and do a .upper to get the values given to lowercase


    return{string.upper() for string in val_in if string == string.lower()}
    #pass
