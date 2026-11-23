import sqlite3
import pytest
import exercise4
from exercise4 import *

def test_no_hardcoded_password():
    import inspect
    assert "admin123" not in inspect.getsource(exercise4)
def test_no_sql_injection():
    db=sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('ana','ana@mail.com')")
    assert find_user(db,"x' OR '1'='1") is None
    assert find_user(db,"ana") is not None
