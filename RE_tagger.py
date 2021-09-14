# A Python Script to Replace Able Kirby
# Rare Encounter Post-production tools
# September 14, 2021
# Able Kirby

from mutagen.id3 import ID3, TPE1, TIT2, TALB, TYER, TRCK, COMM, TCOP, TIT3, USLT
import sys
from datetime import datetime


class reep:
    def __init__(self):
        self.artist_name = "ablekirby and coldacid"
        self.album_title = "Rare Encounter Podcast"

        now = datetime.now()
        self.date = now.strftime("%Y")
        self.comment = "Rare Encounter Podcast, with ablekirby and coldacid."
        self.copyright = "Rare Encounter Podcast"
        self.subtitle = "AbleKirby and coldacid converse on anime they watch, books and manga they read, games they play, and all the tech stuff that they come across."
        self.unsynced_lyrics = "AbleKirby and coldacid converse on anime they watch, books and manga they read, games they play, and all the tech stuff that they come across."
        self.track_num = 0
        self.track_title = "Untitled Encounter"

    def write_tags(self):

        # there is no try [block]
        mytag = ID3(self.fn)
        #mytag.delall()
        mytag.add(TPE1(encoding=3, text=self.artist_name))
        mytag.add(TIT2(encoding=3, text=self.track_title))
        mytag.add(TALB(encoding=3, text=self.album_title))
        mytag.add(TYER(encoding=3, text=self.date))
        mytag.add(TRCK(encoding=3, text=str(self.track_num)))
        mytag.add(COMM(encoding=3, text=str(self.comment)))
        mytag.add(TCOP(encoding=3, text=str(self.copyright)))
        mytag.add(TIT3(encoding=3, text=str(self.subtitle)))
        mytag.add(USLT(encoding=3, text=str(self.unsynced_lyrics)))
        mytag.save()

    @staticmethod
    def new(fn,num,title):
        encounter = reep()
        encounter.fn = fn
        encounter.track_num = num
        encounter.track_title = "Encounter #" + str(num) + " " + title
        return encounter

sexualencounter = reep.new(sys.argv[1], int(sys.argv[2]), sys.argv[3])
sexualencounter.write_tags()