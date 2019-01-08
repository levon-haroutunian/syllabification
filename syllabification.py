# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:07:51 2018

@author: Levon
"""

from collections import namedtuple

# sonority key:
stop = 0
fric = 1 #includes affricates
nasal = 2
liquid = 3
rhotic = 4
glide = 5
vowel = 6

# vc = vowel or consonant
# s = sonority, based on key above
Sound = namedtuple('Sound', ['vc', 's'])

sounds = { "a": Sound("v", vowel), "e": Sound("v", vowel), "i": Sound("v", vowel),
          "o": Sound("v", vowel), "u": Sound("v", vowel),
          "b": Sound("c", stop), "c": Sound("c", stop), "d": Sound("c", stop),
          "f": Sound("c", fric), "g": Sound("c", stop), "h": Sound("c", fric),
          "j": Sound("c", fric), "k": Sound("c", stop), "l": Sound("c", liquid),
          "m": Sound("c", nasal), "n": Sound("c", nasal), "p": Sound("c", stop),
          "q": Sound("c", stop), "r": Sound("c", rhotic), "s": Sound("c", fric),
          "t": Sound("c", stop), "v": Sound("c", fric), "w": Sound("c", glide),
          "x": Sound("c", fric), "y": Sound("c", glide), "z": Sound("c", fric)}


class Syllable:
    def __init__(self, nucleus):
        self.nucleus = nucleus
        self.onset = ''
        self.coda = ''
        
    def __repr__(self):
        return self.onset + self.nucleus + self.coda
    
    def set_onset(self, onset):
        self.onset = onset
        
    def set_coda(self, coda):
        self.coda = coda
        
    def get_nucleus(self): return self.nucleus
    
    def get_onset(self): return self.onset
    
    def get_coda(self): return self.coda

def syllabify(word):
    result = []
    word = word.lower()
    word = word.replace("'", "")
    
    # if hyphen found, syllabify both parts separately
    hyphen = word.find("-")
    
    if hyphen != -1:
        return(syllabify(word[:hyphen])+ syllabify(word[hyphen+1:]))
            
    #edge case: 0 or 1 letter word
    if len(word) <= 1:
        new_syllable = Syllable(word)
        return [new_syllable]
    
    
    letters_used = [False for letter in range(len(word))]

    
    position = 0
    while position < len(word):
    # find nuclei
    # note: conditions are split for ease of reading
    
        nucleus = False
        # non-e vowels
        if sounds[word[position]].vc == "v" and word[position] != "e":
            nucleus = True
        # y as possible vowel
        elif word[position] == "y": 
            # medial y
            if position > 0 and position < len(word)-1 and \
            sounds[word[position-1]].vc == sounds[word[position +1]].vc == "c":
                nucleus = True
            # word final y
            elif position == len(word)-1 and sounds[word[position-1]].vc == "c":
                nucleus = True
        # e
        # TODO: this area needs further refinement to handle words like
        # 'barge' and 'marble'
        elif word[position] == "e":
            # medial e
            if position != len(word)-1:
                nucleus = True
            # word final e
            elif len(result) == 0 or sounds[word[position-2]].vc == "c":
                nucleus = True
            
        if nucleus:
            nucleus_str = str(word[position])
            end = position+1
            while end < len(word) and sounds[word[end]].vc == "v":
                nucleus_str += word[end]
                end += 1
                
            new_syllable = Syllable(nucleus_str)
            
            # create onset using SSP
            # TODO: needs further refinement to deal with nasal clusters
            start = position
            if position > 0:
                while start > 0 and sounds[word[start-1]].s <= sounds[word[start]].s \
                    and not letters_used[start-1]:
                        start -= 1
            
                 # syllable-initial 's' violates SSP if it appears 
                 # before a voiceless stop      
                while start > 0 and (word[start-1] == "s" and word[start] in ['t', 'p','k', 'c', 'q']):
                    start -= 1
                    
                # wh digraph
                if start > 0 and word[start-1] == "w" and word[start] == "h":
                    start -= 1
                        
                new_syllable.set_onset(word[start:position])
            result.append(new_syllable)

            for num in range(start, end):
                letters_used[num] = True
                
            
            position = end
            
        else:
            position += 1
            

    # find codas
    position = 0
    for syllable in result:
        # move to end of onset+nucleus set already found
        syl_str = str(syllable)
        position += len(syl_str)
        
        coda = ''
        while position < len(word) and not letters_used[position]:
            coda += word[position]
            letters_used[position] = True
            position += 1
            
        syllable.set_coda(coda)
        
    return result


