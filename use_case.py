'''
typing example & decorator test
'''
import numpy as np
from time import time
from typing import Optional, List, Dict, Tuple, Set, Union, Callable, Iterable, Any
from utils import test


class ClassA:
    '''
    simple class not meaning
    '''

    a = 0
    b = 1


class SampleClass:
    '''
    write note, argument info, example
    '''

    def __init__(
        self,
        arg1: int,
        arg2: bool,
        arg3: str,
        arg4: float,
        arg5: np.ndarray,
        arg7: List[int],
        arg8: Dict[str, str],
        arg9: Set[float],
        arg10: Tuple[bool],
        arg11: Optional[int],
        arg12: Union[str, int],
        arg13: Union[List[int], Set[bool]],
        arg14: ClassA,
        arg15: Callable[[int, bool], List[int]] = None,
        arg16: Iterable[int] = None,
        arg17: Any = None,
        arg19: int = 0,
        arg20: float = 1.2,
        arg21: List[int] = [1, 2, 3],
    ):
        '''
        nothing
        '''

    @staticmethod
    def function1(input_: np.ndarray) -> np.ndarray:
        '''
        multiply 2
        '''
        return input_ * 2

    @staticmethod
    def function2(input_: int) -> float:
        '''
        cast float
        '''
        return float(input_)

    def static_method_test(self):
        '''
        just execute function1, function2
        '''
        fnc1_result = self.function1(np.array([1, 2]))
        fnc2_result = self.function2(2)
        print(f'{fnc1_result}, {fnc2_result}')

    @classmethod
    def cls_mtd(cls):
        '''
        class_method test
        '''
        print(cls.__name__)


def elapsed_time(func: Callable):
    '''
    elapsed time decorator
    '''
    start = time()
    return_value = func
    end = time()

    print(f'{end - start} sec')
    return return_value


@elapsed_time
def summation(value1: float, value2: float):
    '''
    simple summation function
    '''
    return value1 + value2


RESULT = summation(3, 2)
print(RESULT)

if __name__ == '__main__':
    test(__file__)
    obj = SampleClass(
        1,
        True,
        'a',
        5,
        np.array([1, 2]),
        [1, 2],
        {'1': 'a'},
        {1, 2},
        (True,),
        None,
        'b',
        [1, 2, 3],
        ClassA(),
    )

    print(SampleClass.cls_mtd())
    print(obj.static_method_test())
    print(obj.function1(1))
