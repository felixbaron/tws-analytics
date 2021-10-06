"""
Run unittest located at 'test' directory and restart when file changes.
This script is meant to support automated testing in dev mode.
"""
import os

def test_runner():
    """ Execute command in temrinal
    """
    command = 'nodemon -x "python -m unittest discover test" -e .py'
    os.system(command)

if __name__ == "__main__":
    test_runner()
