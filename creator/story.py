from typing import Dict

from creator.variable import Variable


class Story:
    __variables: Dict[str, Variable]

    def __init__(self, variables: dict) -> None:
        self.__variables = variables
