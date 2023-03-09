"""Main module."""
from string import Template
from copy import copy


COUNT = 0


def decorator(func):
    """Counts calls."""
    def count(self):
        global COUNT
        COUNT += 1
        func(self)
    return count


class Tool:
    """Class for tool."""

    def __init__(self, tag, name, count):
        self.tag = tag
        self.name = name
        self.count = count

    def __str__(self):
        return f'#{self.tag}: {self.name} - {self.count}.'


class ToolBox:
    """Class for the box of tools."""

    def __init__(self):
        self.tools = [Tool(1, 'hammer', 0), Tool(2, 'screwdriver', 8), Tool(3, 'jigsaw', -5), Tool(4, 'screw', 850)]
        self.name = "Toolbox #1.\n"

    def __copy__(self):
        new_box = ToolBox()
        new_box.tools = [Tool(1, 'hammer', 1), Tool(2, 'screwdriver', 1), Tool(3, 'jigsaw', 1), Tool(4, 'screw', 20)]
        new_box.name = "Copy of " + self.name
        return new_box

    def __str__(self):
        return f"""{self.name}
        - {self.tools[0]};
        - {self.tools[1]};
        - {self.tools[2]};
        - {self.tools[3]};
        """

    @decorator
    def print_classic(self):
        print("#%d: Name: %s, count: %d" % (self.tools[0].tag, self.tools[0].name, self.tools[0].count))

    @decorator
    def print_modern(self):
        print("#{0.tag}: Name: {0.name}, count: {0.count}".format(self.tools[1]))

    @decorator
    def print_literal(self):
        print(f'#{self.tools[2].tag}: Name: {self.tools[2].name}, count: {self.tools[2].count}')

    @decorator
    def print_tmpl(self):
        temp = Template("#$tag: Name: $name, count: $count\n")
        print(temp.substitute(tag=self.tools[3].tag, name=self.tools[3].name, count=self.tools[3].count))


if __name__ == '__main__':
    """Start of the program."""

    my_box = ToolBox()
    my_box.print_classic()
    my_box.print_modern()
    my_box.print_literal()
    my_box.print_tmpl()

    for tool in my_box.tools:
        try:
            assert tool.count != 0, f"Not enough tools: {tool.name}"
            assert tool.count > 0, f"Invalid amount: {tool.name}"
        except AssertionError as ex:
            print(ex.args[0])
        except TypeError as ex:
            print(ex.args[0])

    print(f"\nCounter value is now: {COUNT}\n")
    print(my_box)
    second_box = copy(my_box)
    print(second_box)
    third_box = copy(second_box)
    print(third_box)
