# Rules-based syllabification
The purpose of this project is to predict syllable boundaries given the spelling of an English word. It takes a the written representation of a single word as its input, and produces a list of clusters of letters that each roughly represent a single syllable. 

I used a rules-based system to accomplish this, relying mainly on the Sonority Sequencing Principle and the Maximal Onset Principle, along with conventions of English spelling.

I completed this project in early 2019 before I began my master's degree. I intended for this project as a baseline to represent my skills before my graduate coursework, particularly before my coursework in machine learning.

## Format
To get the estimated syllabification of a word, call syllabification.syllabify(word), where word is a string containing no whitespace.

## Testing and limitations
Included in this repo is a file that demonstrates how this algorithm syllabifies common English words. The word list was generated by SCOWL (size 10, no diacritics, all spellings), and was only altered to remove the header -- no words were removed or changed.

In that file, you will see which kinds of words are and are not suitable for syllabification using this method. While this algorithm has a reasonable rate of success given its relative crudeness, it is not able to handle the following categories of words: abbreviations that contain no vowels (like "Mr."), compounds that have a first component ending in 'e' (like "somebody"), words with non-initial syllables that have no onsets (like "pious"), and others.

## Current status
The current version of this project is fully operational. I do not intend to make any further updates.