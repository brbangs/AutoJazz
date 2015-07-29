class harmony:
    """This class deals with tones and harmony, as opposed to rhythm.
    noteget() Returns the distance (in half steps) of a note from 'middle a'.
        Notes below 'middle a' have negative values.
        Input is in the form of a string.
        e.g. noteget('aaasharp') returns 25.
             noteget('GG') returns -14.
    chordget() Returns a list of the note values of any chord in self.chords,
        in any key or octave.
        e.g. chordget('aamajt') returns [12,16,19]."""
    def __init__(self):
         
        self.notes = {'a':0,
        'b':2,
        'c':3,
        'd':5,
        'e':7,
        'f':8,
        'g':10}
        
        self.backnotes = {0:'a',
        2:'b',
        3:'c',
        5:'d',
        7:'e',
        8:'f',
        10:'g'}
        
        self.chords = {
        'majt':[0,4,7], 
        'mint':[0,3,7],
        'majaugt':[0,4,8],
        'majdimt':[0,4,6],
        'mindimt':[0,3,6],
        'maj7':[0,4,7,10],
        'maj7m':[0,4,7,11],
        'min7':[0,3,7,10],
        'min7m':[0,3,7,11],
        'maj6':[0,4,7,9],
        'min6':[0,3,7,9]}
        
        
    def noteget(self,note):
        tone = note[0]
        basicNote = tone.lower()                    #Gets first (lower case) letter (generalized note) of note name.
        basicNumber =  self.notes[basicNote]    #Gets the note number corresponding with the middle-C octave note.
        
        ###############The following "If/Else" block determines whether the note should be made lower or higher using Case of beginning letter.
        
        if(tone.isupper()):
            octShift = -12
            downShift = -12
        else:
            octShift = 12
            downShift = 0
        #The following "while loop" moves the note the proper number of octaves up or down, depending on the number of key letters.
        octave = 0
        self.index = 1                                  ###### This eventually acts as a placeholder to find accidental in chord names
        while((self.index < len(note)) and (note[self.index] == note[self.index-1])):
                
                octave = octave + octShift
                
                self.index = self.index + 1
        
        #### The following system figures out the value for the accidental.
        #This figures out whether there is any accidental at all:
        try:
            accident = note[self.index]
        except:
            accident = 0
        
        #This figures out what the accidental's value should be:
        if (accident == 's'):
            accidental = 1
        elif (accident == 'f'):
            accidental = -1
        elif (accident == 'l'):
            accidental = -13  # This is to deal with 'fflat'.
            self.index = self.index - 1   # This fixes a glitch with the self.index that affects 'chordget'.  (Key error: 'latmajt'.)     
        else:
            accidental = 0
        
        # Finally, all of the elements are added together:
        
        notenumber = basicNumber + octave + downShift + accidental
        
        return notenumber

    def notename(self,notenumber):
        
        octave = abs(notenumber/12)
        note = abs(notenumber%12)
        accidental = ''
        basicNote = ''
        try: 
            basicNote = self.backnotes[note]
        except:
            note = note-1
            basicNote = self.backnotes[note]
            accidental = 'sharp'
        
        if (notenumber < 0):
            
            basicNote = basicNote.upper()
            octave = octave - 1

        letters = octave * basicNote
        
        notename = letters + basicNote + accidental
        
        return notename
        
    def chordname(self,chordlist):
        
        chordnotes = []
        
        for notenumber in chordlist:
            
            notename = self.notename(notenumber)
            
            chordnotes.append(notename)
            
        return chordnotes
              
          
    def chordget(self,chord):  
        ########################################FINDER FINDS THE NOTES OF ANY TYPE OF CHORD IN ANY KEY. 
        ########################################The following  looks up the keynote using 'noteget()'
        keynote = self.noteget(chord)
        ########################################The following if/else block gets the keynote of the chord.
        ######################################## Distinguishes between sharps and flats, adds and subtracts values accordingly.
        if(chord[self.index] == 's'):
            ctype = chord[(self.index + 5):]                                         
        elif(chord[self.index] == 'f'):
            ctype = chord[(self.index + 4):]
        else:  
            ctype = chord[(self.index):] 
        ######################################## Set up some more variables:
        chordnotes = self.chords[ctype]
                                                # Looks up chord type in dictionary, gets list of numbers of each chord note.
        chordout = []
        ######################################### The following FOR loop adds the Key note number to each of the chords numbers, thus shifting it up (eventually down):
        for note in chordnotes:
            
             note = note + keynote
             
             chordout.append(note)
             
        return chordout
        
    def chordnotes(self,chord):
        
        notes = self.chordname(self.chordget(chord))
        
        return notes