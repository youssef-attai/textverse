from creator.story import Story


class Option:
    __story: Story
    __text: str

    def __init__(self, story: Story, text: str) -> None:
        self.__story = story
        self.__text = text
