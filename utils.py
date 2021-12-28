''''''
import os


def test(file_name: str):
    '''
    pylint, mypy test code
    '''
    os.system('echo pylint start')
    os.system(f'pylint {file_name}')
    os.system('echo mypy start')
    os.system('echo *************')
    os.system(f'mypy {file_name}')
    os.system('echo ------------------------------------------------------------------')
