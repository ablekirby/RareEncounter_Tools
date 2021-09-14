# A Python Script to Replace Able Kirby
# Rare Encounter Post-production tools
# September 14, 2021
# Able Kirby

from mutagen.id3 import ID3, TPE1, TIT2, TALB, TYER, TRCK, COMM, TCOP, TIT3, USLT, APIC
import sys
from datetime import datetime

class reep:
    def __init__(self):
        self.artist_name = "Able Kirby and coldacid"
        self.album_title = "Rare Encounter Podcast"

        now = datetime.now()
        self.date = now.strftime("%Y") # All we use for Date is the year

        self.comment = "Rare Encounter Podcast, with Able Kirby and coldacid."
        self.copyright = "Rare Encounter Podcast"
        self.subtitle = "Able Kirby and coldacid converse on anime they watch, books and manga they read, games they play, and all the tech stuff that they come across."
        self.unsynced_lyrics = "Able Kirby and coldacid converse on anime they watch, books and manga they read, games they play, and all the tech stuff that they come across."
        self.track_num = 0
        self.track_title = "Untitled Encounter"

    def write_tags(self):

        # there is no try
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

        imgfn = ".\logo_alt2_scaled.jpg"
        with open(imgfn, 'rb') as albumart:
            mytag['APIC'] = APIC(
                            encoding=3,
                            mime='image/jpeg',
                            type=3, desc=u'Cover',
                            data=albumart.read()
                            )

        mytag.save()

    @staticmethod
    def new(fn,num,title):
        encounter = reep()
        encounter.fn = fn
        encounter.track_num = num
        encounter.track_title = "Encounter #" + str(num) + " " + title
        return encounter


if len(sys.argv) != 4:
    print("\nUsage: RE_tagger.py [mp3 file name] [encounter number] [title]\n\n")

else:
    print("Tagging " + sys.argv[1] + " With ID3 info.")
    print("Encounter Number is " + sys.argv[2])
    print("Encounter Title: " + sys.argv[3])
    myreep = reep.new(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    print("Writing to disk...")
    myreep.write_tags()
    print("Done.")
