EncodedText = "###!!@mocleW EPGTQ!!!6789"
Core_Part = EncodedText[6:18]
First_Word = Core_Part.split(' ')[0]
Second_Word = Core_Part.split(' ')[1]

First_Word_Decoded = First_Word[::-1]

Decoded_Text = First_Word_Decoded + " " + Second_Word
print(Decoded_Text)
