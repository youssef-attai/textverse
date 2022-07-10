from typing import List

from creator.option import Option
from creator.story import Story


class Node:
    __node_id: int
    __story: Story
    __text: str
    __options: list[Option]
    __branches: list['Node']
    __parents: list['Node']

    def __init__(self, story: Story, text: str, options: List[Option]) -> None:
        self.__story = story
        self.__text = text
        self.__options = options
        self.__branches = list()
        self.__parents = list()
        self.__node_id = self.__story.new_node_id()

    def set_text(self, text: str) -> None:
        self.__text = text

    def get_text(self) -> str:
        return self.__text

    def add_option(self, option: Option) -> None:
        self.__options.append(option)

    def add_branch(self, branch: 'Node') -> None:
        self.__branches.append(branch)

    def add_parent(self, parent: 'Node') -> None:
        self.__parents.append(parent)
