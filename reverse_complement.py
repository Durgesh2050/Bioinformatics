# Input will be a pattern
# Output will be its reverse complement
#reverse complement means    A --->T; T--->A; G--->C; C---> G

#---------------------------------------------reverse of the pattern---------------------------------------------------------------

# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    rev_Pattern = Pattern[::-1]
    return rev_Pattern
    
    
#-------------------------------------------complement of the pattern---------------------------------------------------------------

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).

def Complement(Pattern):
    complement = {"A" : "T", "T":"A", "C":"G", "G":"C"}
    newstring = "".join([complement[Pattern[i]] for i in range(len(Pattern))])
    return newstring
    
#-------------------------------------------combine the above function to find reverse complement------------------------------------

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern
