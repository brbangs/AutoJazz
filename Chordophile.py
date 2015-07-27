##### Make a dictionary with notes corresponding to pitches (inputs for MIDIutil)

#################Hey Joe! This program lets you find the 'note numbers' for any defined chord in any key! Try typing something like:

#chor=chord()
#chor.finder('insertnoteheremajt') for example chor.finder('amajt'). You can also change the  chord type, e.g. chor.finder('amaj7m')
# You should get the 'numbers' as an output.


class noteswehg:
    def __init__(self):
        
        self.notes = {'a':0,
        'b':2,
        'c':3,
        'd':5,
        'e':7,
        'f':8,
        'g':10}
     
        
        
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
        index = 1
        while((index < len(note)) and (note[index] == note[index-1])):
                
                octave = octave + octShift
                
                index = index + 1
        
        #### The following system figures out the value for the accidental.
        #This figures out whether there is any accidental at all:
        try:
            accident = note[index]
        except:
            accident = 0
        
        #This figures out what the accidental's value should be:
        if (accident == 's'):
            accidental = 1
        elif (accident == 'f'):
            accidental = -1
        elif (accident == 'l'):
            accidental = -13                 # This is to deal with 'fflat'.
        else:
            accidental = 0
        
        # Finally, all of the elements are added together:
        
        notenumber = basicNumber + octave + downShift + accidental
        
        return notenumber















########################USE TWO INSTANCES: NOTE = CHORD(), CHORD = CHORD(). RENAME THE CLASS TO SOMETHING MORE GENERAL.
########################THAT WAY, CAN USE FINDER AND OTHER FUNCTIONS ON NOTES AND CHORDS.
class chord:
    
    def __init__(self):
        
         self.notes = {
        'a':0,
        'b':2,
        'c':3,
        'd':5,
        'e':7,
        'f':8,
        'g':10}
        
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
            

        
    def chordget(self,chord):  
        ########################################FINDER FINDS THE NOTES OF ANY TYPE OF CHORD IN ANY KEY. 
        
        ########################################The following if/else block gets the keynote of the chord.
        ######################################## Distinguishes between sharps and flats, adds and subtracts values accordingly.
        if(chord[1] == 's'):
            ctype = chord[6:]                                         
            accidental = 1
        elif(chord[1] == 'f'):
            ctype = chord[5:]
            accidental = -1
        else:  
            ckey = chord[0]
            ctype = chord[1:] 
            accidental = 0
        ######################################## Set up some more variables:
        ckey = chord[0]
                                                # Gets the keynote of the chord without sharp or flat. The above loop handles accidentals.
        steps = self.notes[ckey]
                                                # Finds the 'number' of the keynote by looking it up in the note-number dictionary.
        chordnotes = self.chords[ctype]
                                                # Looks up chord type in dictionary, gets list of numbers of each chord note.
        chordout = []
        ######################################### The following FOR loop adds the Key note number to each of the chords numbers, thus shifting it up (eventually down):
        for note in chordnotes:
            
             note = note + steps + accidental
             
             chordout.append(note)
             
        return chordout
        
             
               
        
        
        
        
        
        
        
    
    

        
        
    
        
        
    
    