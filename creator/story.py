from typing import Dict

from creator.node import Node
from creator.variable import Variable


class Story:
    __root: Node
    __current_node: Node
    __variables: Dict[str, Variable]

    def __init__(self, root: Node, variables: dict) -> None:
        self.__latest_node_id = 0
        self.__root = root
        self.__variables = variables
        # TODO: Load current node from some kind of storage (based on user progress of course)
        self.__current_node = self.__root

    def new_node_id(self):
        self.__latest_node_id += 1
        return self.__latest_node_id
