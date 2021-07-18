# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text

#first we find total k-mer and its frequency
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    
    return freq

# second we find the maximu frequency words


#--------------------------------------------------------MAIN FUNCTION---------------------------------------------------------

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    
    m = max(freq.values())                           #to find max. frequency value integer
    
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

