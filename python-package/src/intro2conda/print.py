#!/bin/bash
import os
from pprint import pprint


def customprint(string: str):
    """Prints string depending on an environment variable."""

    # Environment variable specific import. First value tries to get
    # environment variable if not defined set to normal
    PSTYLE = os.getenv("PSTYLE", 'NORMAL')

    # Print depending on the environment variable
    if PSTYLE == 'PRETTY':
        pprint(string)
    else:
        print(string)

    return None
