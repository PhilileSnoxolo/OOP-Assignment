class Music:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
        self.genre = genre
        self.is_playing = False
        self.streams = 0
    
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.streams += 1
            return f"🎵 Now playing: {self.title} by {self.artist}"
        return "⏸️ Music is already playing"
    
    def pause(self):
        if self.is_playing:
            self.is_playing = False
            return "⏸️ Music paused"
        return "▶️ Music is already paused"
    
    def get_duration(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"
    
    def info(self):
        return f"""
        {self.title} ({self.genre}) 
        Artist: {self.artist}
        Duration: {self.get_duration()}
        Streams: {self.streams:,}
        """


# Inheritance example - Pop Music Special Edition
class PopMusic(Music):
    def __init__(self, title, artist, duration, genre="Pop", featured_artist=None):
        super().__init__(title, artist, duration, genre)
        self.featured_artist = featured_artist
        self.is_remix = False
    
    def make_remix(self):
        self.is_remix = True
        return f"♬ Created remix version of {self.title}"
    
    def info(self):  # Overriding the parent method
        base_info = super().info()
        features = f"\nFeaturing: {self.featured_artist}" if self.featured_artist else ""
        remix_note = "\n★ REMIX VERSION" if self.is_remix else ""
        return base_info + features + remix_note


# Example usage with Taylor Swift
if __name__ == "__main__":
    # Taylor Swift's pop song
    anti_hero = PopMusic("Anti-Hero", "Taylor Swift", 201, "Pop")
    print(anti_hero.play())
    print(anti_hero.play())  # Try to play again
    print(anti_hero.pause())
    print(anti_hero.info())
    
   
    
    # Simulate multiple streams
    for _ in range(5):
        anti_hero.play()
        anti_hero.pause()
    print(f"\nAnti-Hero total streams: {anti_hero.streams}")