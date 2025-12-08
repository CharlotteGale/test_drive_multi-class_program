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
        #   self.entry: empty list
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

```