#to find number of time a k-mer appear in the sequence

k is the mer unit you want like  3-mer AAT  CGC CCG AAG etc    and 5-mer like AAATG   TGAAA etc..
#text = sequence

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)       #length of the text or sequence
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    
    return freq
