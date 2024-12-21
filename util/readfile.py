import os
import inspect

def read_file(file: str):
    """
    Opens and returns the input.txt file from the directory of the calling script.

    Returns:
        file object: The opened file object

    Raises:
        FileNotFoundError: If input.txt cannot be found
    """
    caller_frame = inspect.stack()[1]
    caller_path = os.path.dirname(os.path.abspath(caller_frame.filename))

    input_path = os.path.join(caller_path, file)

    try:
        return open(input_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input.txt in {caller_path}")