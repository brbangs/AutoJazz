'''
Joseph DellaMorte
SerialBytes
June 17,2015
'''
####            Code Tutorials 2
#### a couple of things you might find usefull

'spoiler ALERT!!!'
###DICTIONARIES CAN WORK BACKWARDS TOO!!!!
#look at the example dictionary in the bottom
# you can have     'he':34    and   34:'he'
'strings are not the only things that can be dictionary keys!!!'


#as I have demonstrated above    '''    ''' triple quotes  or   """   """   denote a string that can span many lines and enters are included so I could print a paragraph

#like this
paragraph1='''
Welcome to this tutorial.
this tutorial is a free tutorial brought to you by SerialBytes,
a world leader in basically nothing ... yet.
'''

print("printing paragraph 1")
print("")   #<== printing nothing to get an extra line between text
print(paragraph1)

#though you may never see it, computers see enters and/or returns as a character just like i or j.

# it is a special character and is denoted by a     \n

#when ever a computer reads   \n    within a string it looks exactly like when you press enter on the keyboard.

#we can use this character to make a duplicate of the    paragraph1     above by using this     \n    character and keep the string in a single line

paragraph2='Welcome to this tutorial.\nthis tutorial is a free tutorial brought to you by SerialBytes,\na world leader in basically nothing ... yet.'




#putting a \n at the end of this string allows us to double space between prints without having a print("")
print("printing paragraph 2\n")
#####print("")     <== we don't need this any longer
print(paragraph2)


############   as a note concerning last tutorial, lists     cottoncandy = [1,2,3,'hi',[1,2],5]     have order and can be indexed or refered to by where they are in the list...
# the 0th element = 1   the 1st element = 2 ... and so on
#  cottoncandy[0] = 1    cottoncandy[1] = 2 ... and so on

#### dictionaries...    bigheavybook = {'hi':'a word of greeting'     ,   5:'five'   ,   'dictionary':{'one':1,'two':2}   ,   34:'he'}
##   dictionaries don't have order, you can't index them like lists, but are still incredibly usefull when orginizing data.
## because of this lack of sequential order when you print a dictionary it might not always print out in the same order and...
#looking for elements by location in the dictionary does not work


# when working with dictionaries you must use a key from within the dictionary
#  bigheavybook['hi'] = 'a word of greeting'      or     bigheavybook['five'] = 5






