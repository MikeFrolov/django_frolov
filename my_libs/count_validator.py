"""
This program works if you need to check the input parameter for the fact that it is an integer from 1 to 100
"""


def count_valid(count) -> str:
    if not count:
        return '<p>Count not entered!</p>'
    if isinstance(count, str):
        try:
            int(count)
        except ValueError:
            return '<p>Count must be an integer!</p>'
        else:
            if 1 > int(count) or int(count) > 100:
                return '<p>Count must bу greater than 0 and no greater than 100</p>'

        return str(count)
