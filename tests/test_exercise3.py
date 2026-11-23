import sqlite3
import pytest
import exercise3
from exercise3 import *

def test_average_empty(): assert average([]) == 0
def test_first_word_empty(): assert first_word("") == ""
def test_percent_zero(): assert percent(1,0) == 0
