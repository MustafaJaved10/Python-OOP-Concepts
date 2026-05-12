# ============================================
#   PROJECT: PLAYLIST SYSTEM
#   Topic: Classes, Lists, Methods
#   By: Mustafa Javed
# ============================================


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
        else:
            print(f"Song '{song}' not found in playlist")

    def show_songs(self):
        print(f"\n🎵 Playlist: {self.name}")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"  {i}. {song}")
        else:
            print("  (empty)")


# ── Test ──
p1 = Playlist("Mustafa's Best")
p1.add("Rock")
p1.add("Believer")
p1.add("Levitating")
p1.remove("Rock")
p1.show_songs()
