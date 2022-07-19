import sys

class Error:
    def __init__(self, msg):
        print(msg)
        sys.exit(1)
