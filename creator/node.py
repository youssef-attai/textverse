from typing import List

from creator.option import Option


class Node:
    __text: str
    __options: list[Option]
    __branches: list['Node']

    def __init__(self, text: str, options: List[Option]) -> None:
        self.__text = text
        self.__options = options
        self.__branches = list()

    def set_text(self, text: str) -> None:
        self.__text = text

    def get_text(self) -> str:
        return self.__text

    def add_option(self, option: Option) -> None:
        self.__options.append(option)

    def add_branch(self, branch: 'Node') -> None:
        self.__branches.append(branch)
