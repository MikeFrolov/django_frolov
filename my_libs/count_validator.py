"""
This program works if you need to check the input parameter for the fact that it is an integer from 1 to 100
"""


def count_valid(count) -> str:
    if not count:
        return '<br><br><h2 align=center>Please enter a value for count in url!</h2>'
    if isinstance(count, str):
        try:
            int(count)
        except ValueError:
            return '<br><br><h2 align=center>Count must be an integer!</h2>'
        else:
            if 2 > int(count) or int(count) > 100:
                return '<br><br><h2 align=center>Count must bу greater than 1 and no greater than 100</h2>'

        return str(count)
