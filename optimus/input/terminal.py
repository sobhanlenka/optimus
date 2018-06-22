from __future__ import unicode_literals
from optimus.input import InputAdapter
from optimus.conversation import Statement
from optimus.utils import input_function


class TerminalAdapter(InputAdapter):
    """
    A simple adapter that allows optimus to
    communicate through the terminal.
    """

    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        user_input = input_function()
        return Statement(user_input)
