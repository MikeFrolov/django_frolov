"""
This program works if you need to check the input parameter for the fact that it is an integer from 1 to 100
"""


def count_valid(count) -> str:
    if not count:
        return 'Please enter a value for count in url!'
    if isinstance(count, str):
        try:
            int(count)
        except ValueError:
            return 'Count must be an integer!'
        else:
            if 2 > int(count) or int(count) > 100:
                return 'Count must bу greater than 1 and no greater than 100'

        return str(count)
