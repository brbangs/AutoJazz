#Notenumber to frequency converter:

class midiprepare:
   
    def __init__(self):
        
        pass
        
    def freqfinder(self,notenumber):
        ### The halfsteps-to-frequency formula:
        ### 440 hz = the frequency of middle a.
        frequency = 440 * pow((pow(2,1.0/12)),notenumber)
    
        return frequency
    