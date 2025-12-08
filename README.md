# Test Drive a Multi-Class Program

## Notes on Behaviour/Interaction
- `Diary()` relies on `DiaryEntry()`
- *Unit tests* can be carried out on **all** `DiaryEntry()` methods
- `Diary()` requires *integration tests*

## Plan for Testing
Unit tests need to be written for the following:
1. `DiaryEntry`s `__init__` method.
2. `DiaryEntry`s `count_words` method.
3. `DiaryEntry`s `reading_time` method.
4. `DiaryEntry`s `reading_chunk` method.
5. Validation check on Type input to `DiaryEntry`
6. Validation check on Type into to `Diary`

> Note: `Diary`s `__init__` method is taking no parameters and doesn't seem to be affecting internal state.
> Note: On further inspection, `Diary` should be initialised with a `list` to store diary entries.

Integration tests need to be written for the following:
1. `Diary`s `add` method.
    > This requires an instance of `DiaryEntry` to complete.
2. `Diary`s `all` method.
    > This requires an instance of `DiaryEntry` to complete.
3. `Diary`s `count_words` method.
    > This requires access to `diary_entry.count_words()`.
4. `Diary`s `reading_time` method.
    > This requires an instance of `DiaryEntry` to complete.
5. `Diary`s `find_best_entry_for_reading_time` method.
    > This requires an instance of `DiaryEntry` to complete.

## Class Interfaces
```python
class Diary:
    def __init__(self):
        # Internal State:
        #   self.entries: empty list
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass
```

```python
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass
```

## Example Tests
```python
"""
Given a title and contents
Check params are stored to the instance
"""
diary_entry = DiaryEntry("title", "contents")

assert diary_entry.title == "title"
assert diary_entry.contents == "contents"
```

```python
"""
Given a title and contents
Returns the word count of contents
"""
diary_entry = DiaryEntry("Wed 3 Dec", "50 words")

assert diary_entry.count_words() == 50
```

```python
"""
Given an int representing words per minute
Returns an estimated reading time for the contents
"""
diary_entry = DiaryEntry("Wed 3 Dec", "500 words.")

assert diary_entry.reading_time(100) == 5.0
assert diary_entry.reading_time(250) == 2.5
assert diary_entry.reading_time(500) == 1.0
```

```python
"""
Given an int for reading words per minute and an int for minutes available to read
returns a snippet of the contents that the reader can read in the available time to read
"""
diary_entry = DiaryEntry("Wed 3 Dec", "500 words.")

assert diary_entry.reading_chunk(10, 5) == "First 50 words"

"""
Continuation of the above test
Returns a block of text, but skips what has already been given until the contents has been fully passed to user.
"""
assert diary_entry.reading_chunk(10, 5) == "Next 50 words"

assert diary_entry.reading_chunk(10, 10) == "Next 100 words"

assert diary_entry.reading_chunk(10, 10) == "Next 100 words"

assert diary_entry.reading_chunk(10, 20) == "Final 200 words"

"""
Continuation of the initial test
Once all contents has been given, it should return to the start
"""
assert diary_entry.reading_chunk(10, 5) == "First 50 words"
```

```python
"""
Given an argument that's not a string
Returns a TypeError
"""
with pytest.raises(TypeError) as e:
    diary_entry = DiaryEntry(3.12, "contents")
error_message = str(e.value)
assert error_message == "Please only input valid strings"
```

```python
"""
On instantiation
Ensure self.entries is initialised.
"""
diary = Diary()
assert diary.entries == []
```

```python
"""
When given an instance of DiaryEntry
Ensure the diary entry is added to self.entries
"""
diary = Diary()
diary_entry = DiaryEntry("title", "contents")

assert diary.add(diary_entry) == [['title', 'contents']]
```

```python
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

assert diary.all() == [["title1", "contents1"], ["title2", "contents2"], ["title3", "contents3"], ["title4", "contents4"]]
```

```python
"""
When given a reading words per minute (`wpm`)
Return how long it will take to read all instances of DiaryEntry stored.
"""
diary = Diary()
diary_entry1 = DiaryEntry("title", "contents of 500 words")
diary_entry2 = DiaryEntry("title2", "contents of 500 words")

diary.add(diary_entry1)
diary.add(diary_entry2)

assert diary.reading_time(200) == 5
```

```python
"""
Given a reading wpm and minutes to read
Return an instance of DiaryEntry that can be read in its entirety within the given minutes.
"""
diary = Diary()
diary_entry1 = DiaryEntry("title1", "contents of 498 words")
diary_entry2 = DiaryEntry("title2", "contents of 502 words")

diary.add(diary_entry1)
diary.add(diary_entry2)

assert diary.find_best_entry_for_reading_time(100, 5) == "contents of 498 words"
assert diary.find_best_entry_for_reading_time(100, 3) == None
```

```python
"""
In the instance that Diary() is passed an object that is not DiaryEntry()
Raise a TypeError
"""
with pytest.raises(TypeError) as e:
    diary.add("contents")
error_message = str(e.value)
assert error_message == "Please input a valid instance of DiaryEntry"
```