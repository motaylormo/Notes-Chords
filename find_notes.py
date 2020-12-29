scale = ("G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#")

# string + fret = note
def findNote(ref, steps):
    note = scale.index(ref) + int(steps * 2)
    while note >= len(scale):
        note -= len(scale)
    return scale[note]

# Class
class Instrument:
    def getstrings(self):
        return self.strings
    def getstringcount(self):
        return len(self.strings)
    def getkind(self):
        return self.kind
        
    def tune(self, strings):
        if len(strings) == self.getstringcount():
            self.strings = strings
        else:
            print("Cannot tune to " + str(strings) + " since the " + self.kind + " has " + str(self.getstringcount()) + " strings.")

# Dulcimer
class Dulcimer(Instrument):
    kind = "dulcimer"
    strings = ['D', 'A', 'D']

class Strumstick(Dulcimer):
    kind = "strumstick"
    strings = ['G', 'D', 'G']
    frets = 12
    
    def getNote(self, string, fret):
        if (not(string in scale)):
            return "string error"
        elif (fret > 12 or fret < 0):
            return "fret error"
        else:
            fretboard = {0 : 0,
                         1 : 1,
                         2 : 2,
                         3 : 2.5,
                         4 : 3.5,
                         5 : 4.5,
                         6 : 5,
                         7 : 5.5,
                         8 : 6,
                         9 : 7,
                        10 : 8,
                        11 : 8.5,
                        12 : 9.5
                    }
            return findNote(string, fretboard[fret])

# Ukulele
class Ukulele(Instrument):
    kind = "ukulele"
    strings = ['G', 'C', 'E', 'A']
    frets = 12

    def getNote(self, string, fret):
        if (not(string in scale)):
            return "string error"
        elif (fret > 12 or fret < 0):
            return "fret error"
        else:
            return findNote(string, (fret * 0.5))



x = Strumstick()
x.tune(['D', 'D', 'D'])
print(x.getstrings())
print(x.getstringcount())


print(x.getNote("D", 1))
#print(getNote("D", 2))
#print(getNote("D", 3))
#print(getNote("D", 4))
#print(getNote("D", 5))
#print(getNote("D", 6))
#print(getNote("D", 7))
#print(getNote("D", 8))
#print(getNote("D", 9))
#print(getNote("D", 10))
#print(getNote("D", 11))
#print(getNote("D", 12))


u = Ukulele()
print(u.getNote("D", 1))
