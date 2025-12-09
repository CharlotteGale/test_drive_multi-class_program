from lib.diary_entry import *
from tests.helpers import *
import pytest

def test_title_and_contents_created_on_init():
    """
    Given a title and contents
    Check params are stored to the instance
    """
    diary_entry = DiaryEntry("title", "contents")

    assert diary_entry.title == "title"
    assert diary_entry.contents == "contents"

def test_word_count_of_contents_returns_integer():
    """
    Given a title and contents
    Returns the word count of contents
    """
    diary_entry = DiaryEntry("Wed 3 Dec", generate_contents(50))

    assert diary_entry.count_words() == 50

def test_return_estimated_reading_time_for_contents():
    """
    Given an int representing words per minute
    Returns an estimated reading time for the contents
    """
    diary_entry = DiaryEntry("Wed 3 Dec", generate_contents(500))

    assert diary_entry.reading_time(100) == 5.0
    assert diary_entry.reading_time(250) == 2.0
    assert diary_entry.reading_time(500) == 1.0