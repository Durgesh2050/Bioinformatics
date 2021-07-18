#Find all occurrences of a pattern in a string.
#Input: Strings Pattern and Genome.
#Output: All starting positions in Genome where Pattern appears as a substring.

def PatternMatching(Pattern, Genome):
    pos = []      # output variable
    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        if Genome[i:i+k] == Pattern:
            pos.append(i)
    return pos
