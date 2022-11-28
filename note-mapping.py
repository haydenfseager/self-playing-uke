#This file maps notes outside of the servo range to the corresponding notes setup up in the top file

# note range 67-73
#     60: C4
#     61: C#4
#     62: D4
#     63: D#4
#     64: E4
#     65: F4
#     66: F#4
#     67: G4
#     68: G#4
#     69: A4
#     70: A#4
#     71: B4
#     72: C5
#     73: C#5

def note_map(song):
    for notes in song:
        if notes[0] < 60 or notes[0] > 73:
            notes[0] = (notes[0] % 12) + 60
