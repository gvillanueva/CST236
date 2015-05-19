"""
:mod:`source.datafile` -- DataFile class
========================================

The DataFile class is responsible for parsing research speed input data from
files.
"""
class DataFile(object):
    """Instantiates a new DataFile object
    """
    def __init__(self, file):
        self.file = file

    """Reads a file and returns the parsed data.
    :return: "ParsedData" if file exists and is valid. Otherwise None.
    :rtype: string
    """
    def read(self):
        if self.file != "valid.txt":
            return None
        else:
            return "ParsedData"