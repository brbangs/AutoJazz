### Following is a simple list of notes, spaced apart by half - steps. 
### Each tone capable of being played corresponds to EXACTLY ONE value, so there is no data overlap. 
### This arrangement will enable the "sliding" of chords and melodies into different keys. 

halfsteps = ['AAA',
 'AAAsharp',
 'BBB',
 'CCC',
 'CCCsharp',
 'DDD',
 'DDDsharp',
 'EEE',
 'FFF',
 'FFFsharp',
 'GGG',
 'GGGsharp',
 'AA',
 'AAsharp',
 'BB',
 'CC',
 'CCsharp',
 'DD',
 'DDsharp',
 'EE',
 'FF',
 'FFsharp',
 'GG',
 'GGsharp',
 'A',
 'Asharp',
 'B',
 'C',
 'Csharp',
 'D',
 'Dsharp',
 'E',
 'F',
 'Fsharp',
 'G',
 'Gsharp',
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
 'gsharp',
 'aa',
 'aasharp',
 'bb',
 'cc',
 'ccsharp',
 'dd',
 'ddsharp',
 'ee',
 'ff',
 'ffsharp',
 'gg',
 'ggsharp',
 'aaa',
 'aaasharp',
 'bbb',
 'ccc',
 'cccsharp',
 'ddd',
 'dddsharp',
 'eee',
 'fff',
 'fffsharp',
 'ggg',
 'gggsharp']




CD = {'A': 24,
 'AA': 12,
 'AAA': 0,
 'AAAsharp': 1,
 'AAsharp': 13,
 'Asharp': 25,
 'B': 26,
 'BB': 14,
 'BBB': 2,
 'C': 27,
 'CC': 15,
 'CCC': 3,
 'CCCsharp': 4,
 'CCsharp': 16,
 'Csharp': 28,
 'D': 29,
 'DD': 17,
 'DDD': 5,
 'DDDsharp': 6,
 'DDsharp': 18,
 'Dsharp': 30,
 'E': 31,
 'EE': 19,
 'EEE': 7,
 'F': 32,
 'FF': 20,
 'FFF': 8,
 'FFFsharp': 9,
 'FFsharp': 21,
 'Fsharp': 33,
 'G': 34,
 'GG': 22,
 'GGG': 10,
 'GGGsharp': 11,
 'GGsharp': 23,
 'Gsharp': 35,
 'a': 36,
 'aa': 48,
 'aaa': 60,
 'aaasharp': 61,
 'aasharp': 49,
 'asharp': 37,
 'b': 38,
 'bb': 50,
 'bbb': 62,
 'c': 39,
 'cc': 51,
 'ccc': 63,
 'cccsharp': 64,
 'ccsharp': 52,
 'csharp': 40,
 'd': 41,
 'dd': 53,
 'ddd': 65,
 'dddsharp': 66,
 'ddsharp': 54,
 'dsharp': 42,
 'e': 43,
 'ee': 55,
 'eee': 67,
 'f': 44,
 'ff': 56,
 'fff': 68,
 'fffsharp': 69,
 'ffsharp': 57,
 'fsharp': 45,
 'g': 46,
 'gg': 58,
 'ggg': 70,
 'gggsharp': 71,
 'ggsharp': 59,
 'gsharp': 47}

chord = 'gchord'



chords = {'cmajt':['c','e','g'],
'csharpmajt': ['csharp','f','gsharp'],
'dmajt':['d','fsharp','a'],
'dsharpmajt': ['dsharp','g','asharp'],
'emajt':['e','gsharp','b'],
'fmajt':['f','a','cc'],
'gmajt':['g','b','dd'],
'amajt':['a','ccsharp','ee'],
'cmaj7':['c','e','g','aasharp']}


index=0

yes_or_no = 'yes'

while (yes_or_no =='yes'):
    print ('                   ')
    print ('Look up chord here:')
    chord_in_question = raw_input()
    notes = chords[chord_in_question]
    print ('Here are the musical notes for the chord:')
    print notes
    print ('Here are the numbers from the dictionary:')
    while (index < len(notes)):
        print [CD[index]]
        index = index + 1
    print('Would you like to look up another chord?')
    index = 0
    yes_or_no= raw_input() 
    
if (yes_or_no != 'yes'):
    print('Alright, forget it!')


### Following is a dictionary of notes corresponding with sound files (eventually). "CD" stands for "Chromatic Dictionary."

#######################################################################################################################################33

import random

import time

while ("chicken" == "chicken"):
    
    chord = 'gchord'
    
    if (chord == 'gchord'):
        
########## get_chord('fchord',75, 'cchord', 20, 'gchord',5,n,0,n,0,n,0)
        
################################################################### Should turn this into a definition: get_chord(chord, percent, chord, percent, chord, percent)
################################################################### Don't forget 'return'.
        
        ################ There should be a percentage-to-number-range converter. Randnum = output. 
        
        randnum = random.randint(0,100)
        
        if (randnum <= 75):
            print('fchord')
            chord = 'fchord'
        
        elif (randnum <= 90):
            print('cchord')
        
        elif (randnum <= 100):
            print('achord')
              
        time.sleep(1)
        
################################################################### Could extend to maybe 7 chords, and then have a "nothing" chord.
################################################################### time.sleep(notedur) Notedur is power of Tempo.. 

##########Start of block:   

def get_chord(c1,p1,c2,p2,c3,p3,c4,p4,c5,p5,c6,p6):
    
    randnum = random.randint(0,100)
    
    percents = [p1,p2,p3,p4,p5,p6]
    percents.sort()
    percents.reverse()
    
    if (randnum <= percents[1]):
        newchord = c1
    
    elif (randnum <= (percents[0] + percents[1])):
        newchord = c2
    
    elif (randnum <= (percents[0] + percents[1] + percents[2])):
        newchord = c3
        
    elif (randnum <= (percents[0] + percents[1] + percents[2] + percents[3])):
        newchord = c4
        
    elif (randnum <= (percents[0] + percents[1] + percents[2] + percents[3] + percents[4])):
        newchord = c5
        
    elif (randnum <= (percents[0] + percents[1] + percents[2] + percents[3] + percents[4] + percents[5])):
        newchord = c6
        
    return newchord


################################## Correspond chords with gotten chords in dictionary???