EncodedText = "##$$$@!yalpstcejorp EPUVT****9887"
Core_Part = EncodedText[7:25]
First_Word = Core_Part.split(' ')[0]
Second_Word = Core_Part.split(' ')[1]

First_Word_Decoded = First_Word[::-1]
Shifted_Vowels = {'E':'A','U':'O'}
for ch in Second_Word:
    if ch in Shifted_Vowels:
        Second_Word = Second_Word.replace(ch, Shifted_Vowels[ch])
DecodedText = First_Word_Decoded + " " + Second_Word
print(DecodedText)
