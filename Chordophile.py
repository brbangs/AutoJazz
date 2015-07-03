##### Make a dictionary with notes corresponding to pitches (inputs for MIDIutil)
##### 

#################Hey Joe! This program lets you find the 'note numbers' for any defined chord in any key! Try typing something like:

#chor=chord()
#chor.finder('insertnoteheremajt') for example chor.finder('amajt'). You can also change the  chord type, e.g. chor.finder('amaj7m')
# You should get the 'numbers' as an output.
# Do I really have to write 'self' before EVERYTHING like I've been doing, though?



class chord:
    
    def __init__(self):
        
        
        self.chords = {
        'majt':[0,4,7], 
        'mint':[0,3,7],
        'majaug':[0,4,8],
        'majdim':[0,4,6],
        'mindim':[0,3,6],
        'maj7':[0,4,7,10],
        'maj7m':[0,4,7,11],
        'min7':[0,3,7,10],
        'min7m':[0,3,7,11],
        'maj6':[0,4,7,9],
        'min6':[0,3,7,9]}
        
        self.notes = {
        'a':0,
        'asharp':1,
        'b':2,
        'c':3,
        'csharp':4,
        'd':5,
        'dsharp':6,
        'e':7,
        'f':8,
        'fsharp':9,
        'g':10,
        'gsharp':11}
        
    def finder(self,chord):
        
        self.chord = chord
        
        self.ckey = (str(self.chord))[0]     
                                                # Gets the first letter of the chord, the keynote ('X'majt)
        
        self.ctype = (str(self.chord))[1:]       
                                                # Gets the chord type, such as 'majt'.
        
        self.steps = self.notes[self.ckey]
                                                # Finds the 'number' of the keynote by looking it up in the note-number dictionary.
        
        self.chordnotes = self.chords[self.ctype]
                                                # Looks up chord type in dictionary, gets list of numbers of each chord note.
        
        self.chordout = []
        ######################################### The following FOR loop adds the Key note number to each of the chords numbers, thus shifting it up (eventually down):
        for self.note in self.chordnotes:
            
             self.note = self.note + self.steps
             
             self.chordout.append(self.note)
             
        return self.chordout
        
    
    
    ####################### THERE IS ONE BIG FLAW: IT CAN'T DEAL WITH SHARPS YET. I'll figure that out tomorrow. :)
             
               
        
        
        
        
        
        
        
    
    

        
        
    
        
        
    
    