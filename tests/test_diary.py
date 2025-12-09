from lib.diary import *
from lib.diary_entry import *
from tests.helpers import *
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

def test_returns_list_of_diary_instances():
    """
    When instances of DiaryEntry are added to the list
    Return a list of the DiaryEntry instances
    """
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "contents1")
    diary_entry2 = DiaryEntry("title2", "contents2")
    diary_entry3 = DiaryEntry("title3", "contents3")
    diary_entry4 = DiaryEntry("title4", "contents4")

    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    diary.add(diary_entry4)

    assert diary.all() == [diary_entry1, diary_entry2, diary_entry3, diary_entry4]

def test_word_count_of_diary_entry_contents():
    """
    When count_words is called
    Return an integer of the summation of all diary_entry.contents
    """
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", generate_contents(500))
    diary_entry2 = DiaryEntry("title2", generate_contents(250))

    diary.add(diary_entry1)
    diary.add(diary_entry2)

    assert diary.count_words() == 750

# @pytest.mark.skip(reason="Waiting for DiaryEntry.count_words()")
def test_returns_how_long_to_read_all_DiaryEntry_instances_stored():
    """
    When given a reading words per minute (`wpm`)
    Return how long it will take to read all instances of DiaryEntry stored.
    """
    diary = Diary()
    diary_entry1 = DiaryEntry("title", generate_contents(500))
    diary_entry2 = DiaryEntry("title2", generate_contents(500))

    diary.add(diary_entry1)
    diary.add(diary_entry2)

    assert diary.reading_time(200) == 5

def test_returns_an_instance_of_DiaryEntry_that_can_be_read_in_the_given_time():
    """
    Given a reading wpm and minutes to read
    Return an instance of DiaryEntry that can be read in its entirety within the given minutes.
    """
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", generate_contents(498))
    diary_entry2 = DiaryEntry("title2", generate_contents(502))

    diary.add(diary_entry1)
    diary.add(diary_entry2)

    assert diary.find_best_entry_for_reading_time(100, 5) == diary_entry1
    assert diary.find_best_entry_for_reading_time(100, 3) == None

def test_returns_type_error_if_instance_passed_not_DiaryEntry():
    """
    In the instance that Diary() is passed an object that is not DiaryEntry()
    Raise a TypeError
    """
    diary = Diary()
    with pytest.raises(TypeError) as e:
        diary.add("contents")
    error_message = str(e.value)
    assert error_message == "Please input a valid instance of DiaryEntry"