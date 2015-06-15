notes = {'AA':None,'BB':None,'CC':None,'DD':None,'EE':None,'FF':None,'GG':None,'A':None,'B':None,'C':None,'D':None,'E':None,'F':None,'G':None,'a':None,'b':None,'c':None,'d':None,'e':None,'f':None,'g':None,'aa':None,'bb':None,'cc':None,'dd':None,'ee':None,'ff':None,'gg':None}
    # x={'key1':value , 'key2':[listEntry1,listEntry2,listEntry3]  ,  'key3':'string'}
    # when you write    x['key1']    it is the same as having the value by it
    # when you write    x.keys()     it will return a list of all the keys   'i called them key one key two key three because that is what they are but you can use any string'
    # when you write    x.values()   it will return a list for all the values. for this example you would get back   [value, [listEntry1,listEntry2,listEntry3],'string']
    # if you want to add something to the x dictionary you write    x['newkey']=newValueStringListorDictionary
    
    # also as a note the extra spaces I put were just to help you see distinctions between things in the text and dictionary, its NOT some strange syntax thing going on
        
    
    
    
    # also in the notes dictionary I wrote, the word    None    shows up, that is a None object (strings, values, dictionaries, lists are all objects) it is really something to show that there is nothing




#I am going to go through all the    keys    of the dictionary    notes   and each one is a string so I am going to add a different string to it 'string1'+'string2'='string1string2'

#made a new dictionary for new notes
newnotes={}

#for loop iterates through the list returned when we write notes.keys() and for each entry will make 3 entries in newnotes
for note in notes.keys():    
    newnotes[note]=None #we copy the key exactly
    newnotes[note+'sharp']=None # we copy the key and append (add on the end) the string 'sharp'
    newnotes[note+'flat']=None  # we copy the key and append the string 'flat'          (you could write    'flat'+note    and that would give you an output of 'flata'  or 'flatBB')
    
print newnotes
print len(newnotes.keys())#prints the length of the list of keys of the dictionary   newnotes

######by the way this short code saved me from writing out 112 words, and only cost me 16 words to write

