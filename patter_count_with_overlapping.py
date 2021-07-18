#to find number of pattern in the sentence with overlapping
#text = text in which pattern to be found
#count number of the pattern in the sentence

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
    
