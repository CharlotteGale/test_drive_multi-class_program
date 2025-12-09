from lib.diary_entry import *

class Diary():
    def __init__(self):
        self.entries = []
        
    def add(self, entry):
        if not isinstance(entry, DiaryEntry):
            raise TypeError("Please input a valid instance of DiaryEntry")
        
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total
    
    def reading_time(self, wpm):
        total = 0
        for entry in self.entries:
            total += entry.reading_time(wpm)
        return total

    def find_best_entry_for_reading_time(self, wpm, minutes):
        best_entry = None

        for entry in self.entries:
            if entry.reading_time(wpm) <= minutes:
                if best_entry == None:
                    best_entry = entry
                else:
                    if entry > best_entry:
                        best_entry = entry
        
        return best_entry