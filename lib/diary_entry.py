class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.current_position = 0

    def count_words(self):
        return len(self.contents.split())
    
    def reading_time(self, wpm):
         return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        all_words = self.contents.split()

        if self.current_position >= len(all_words):
            self.current_position = 0

        chunk_words = all_words[self.current_position : self.current_position + words_can_read]
        self.current_position += words_can_read
        return " ".join(chunk_words)