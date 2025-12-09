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

def test_returns_chunk_and_updates_index_then_restarts():
    """
    Given an int for reading words per minute and an int for minutes available to read
    returns a snippet of the contents that the reader can read in the available time to read
    """
    contents_500 = generate_numbered_contents(500)
    diary_entry = DiaryEntry("Wed 3 Dec", contents_500)

    assert diary_entry.reading_chunk(10, 5) == " ".join(contents_500.split()[ : 50]) # 50

    """
    Continuation of the above test
    Returns a block of text, but skips what has already been given until the contents has been fully passed to user.
    """
    assert diary_entry.reading_chunk(10, 5) == " ".join(contents_500.split()[50 : 100]) # 50

    assert diary_entry.reading_chunk(10, 10) == " ".join(contents_500.split()[100 : 200]) # 100

    assert diary_entry.reading_chunk(10, 10) == " ".join(contents_500.split()[200 : 300]) # 100

    assert diary_entry.reading_chunk(10, 20) == " ".join(contents_500.split()[300 : 500]) # 200

    """
    Continuation of the initial test
    Once all contents has been given, it should return to the start
    """
    assert diary_entry.reading_chunk(10, 5) == " ".join(contents_500.split()[ : 50]) # 50

def test_raises_type_error_if_not_passed_string():
    """
    Given an argument that's not a string
    Returns a TypeError
    """
    with pytest.raises(TypeError) as e:
        diary_entry = DiaryEntry(3.12, "contents")
    error_message = str(e.value)
    assert error_message == "Please only input valid strings"

def test_raises_value_error_on_empty_string():
    """
    Given an empty string as an argument
    Returns a ValueError
    """
    with pytest.raises(ValueError) as e:
        diary_entry = DiaryEntry("", "Contents")
    error_message = str(e.value)
    assert error_message == "Title cannot be empty"