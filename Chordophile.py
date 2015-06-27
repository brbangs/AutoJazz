##### Make a dictionary with notes corresponding to pitches (inputs for MIDIutil)
##### 





class chord:
    
    def __init__(self):
        self.halfsteps = [
        'a',
        'asharp',
        'b',
        'c',
        'csharp',
        'd',
        'dsharp',
        'e',
        'f',
        'fsharp',
        'g',
        'gsharp']
        
        self.chords = {'x':[0],
        'xmajt':[0,4,7], 
        'xmint':[0,3,7],
        'xmajaug':[0,4,8],
        'xmajdim':[0,4,6],
        'xmindim':[0,3,6],
        'xmaj7':[0,4,7,10],
        'xmaj7m':[0,4,7,11],
        'xmin7':[0,3,7,10],
        'xmin7m':[0,3,7,11],
        'xmaj6':[0,4,7,9],
        'xmin6':[0,3,7,9]}
        
    def shifter(self,nots):
        
        
        
    
        
        
    
    