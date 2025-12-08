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

def test_diary_entries_added_to_entries_list():
    """
    When given an instance of DiaryEntry
    Ensure the diary entry is added to self.entries
    """
    diary = Diary()
    diary_entry = DiaryEntry("title", "contents")

    diary.add(diary_entry)

    assert diary_entry in diary.entries