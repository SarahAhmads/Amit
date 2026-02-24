EncodedText = "&&&$gnirts PLIO!!@1234"
Core_Part = EncodedText[4:15]
First_Word = Core_Part.split(' ')[0]
Second_Word = Core_Part.split(' ')[1]

First_Word_Decoded = First_Word[::-1]
Shifted_Vowels = {'I':'E','O':'U'}
for ch in Second_Word:
    if ch in Shifted_Vowels:
        Second_Word = Second_Word.replace(ch, Shifted_Vowels[ch])

DecodedText = First_Word_Decoded + " " + Second_Word
print(DecodedText)
