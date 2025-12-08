from lib.diary import *
from lib.diary_entry import *
import pytest

def test_entries_list_created_on_init():
    """
    On instantiation
    Ensure self.entries is initialised.
    """
    diary = Diary()
    assert diary.entries == []