from typing import AnyStr, Union, Tuple, Match
import re
from plp.errors import *
from plp.utils import *


def greetcheck(text: AnyStr) -> Tuple[bool, Union[Tuple[AnyStr], None]]:
    """
    Checks if string contains greeting
    :param text: Any string type object
    :return: A tuple containing a boolean, a tuple of matches to greetings or None
    """
    expression: Union[Match, None] = re.search(r"((he[nly])+l*o+|hey)", text.lower())
    is_greeting: bool = True if expression else False
    expression: Union[Tuple[AnyStr], None] = expression.groups() if expression else expression

    return is_greeting, expression

print(greetcheck("Hey"))
