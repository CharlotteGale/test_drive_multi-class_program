from lib.diary_entry import *

class Diary():
    def __init__(self):
        self.entries = []
        
    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total
    