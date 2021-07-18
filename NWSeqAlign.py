def NWSeqAlign(seq1,seq2,gap_score=-1,match_score=1,mismatch_score=0):
  seq1,seq2 = list(seq1),list(seq2)
  #<======matrix formation=====>
  matrix = []
  
  for i in range (0,len(seq1)+1):
    k = []
    for j in range(0,len(seq2)+1):
      k.append(0)
    matrix.append(k)


  #<=======Initiation============>
  for l in range(0,len(seq2)+1):
    matrix[0][l] = l*gap_score
  for m in range(1,len(seq1)+1):
    matrix[m][0] = m*gap_score



  #<======Matrix Filling=========>
  for row in range(1,len(seq1)+1):
    for column in range(1,len(seq2)+1):
      up,left,diag = 0,0,0
      
      up = matrix[row-1][column] + gap_score
      left = matrix[row][column-1] + gap_score
      if seq1[row-1] == seq2[column-1]:
        diag = match_score + matrix[row-1][column-1]
      else:
        diag = mismatch_score + matrix[row-1][column-1]
      matrix[row][column] = max(up,left,diag)

  #<=========Backtracing===========>
  
  A,B = Backtracing(seq1,seq2, matrix, gap_score,match_score,mismatch_score)

  return matrix,A,B  #final answer
      


#<========Function for Backtracing=========>
def Backtracing(seq_2,seq_1,matrix,gap,match_score,mismatch_score):
  AlignmentA = ""
  AlignmentB = ""
  d = gap
  row = len(seq_2)
  col = len(seq_1)

  while row>0 and col>0:
    score = matrix[row][col]
    scoreDiag = matrix[row-1][col-1]
    scoreUp = matrix[row][col-1]
    scoreLeft = matrix[row-1][col]

    if score == scoreDiag + Similarity(seq_1[col-1],seq_2[row-1],match_score,mismatch_score):

      AlignmentA = seq_2[row-1] + AlignmentA
      AlignmentB = seq_1[col-1] + AlignmentB
      row-=1
      col-=1

    elif score ==scoreLeft + d:
      AlignmentA = seq_2[row-1] + AlignmentA
      AlignmentB = "-"+ AlignmentB
      row-=1
    elif score == scoreUp + d:

      AlignmentA = "-" + AlignmentA
      AlignmentB = seq_1[col-1]+ AlignmentB
      col-=1 
    
  while row>0:
    AlignmentA = seq_2[row-1] + AlignmentA
    AlignmentB = "-"+ AlignmentB
    row-=1

  while col>0:
    AlignmentA = "-" + AlignmentA
    AlignmentB = seq_1[col-1]+ AlignmentB
    col-=1
  return AlignmentA,AlignmentB


def Similarity(A,B,match_score=1,mismatch_score=0):
  if A == B :
    return match_score
  else:
    return mismatch_score

#<****************==========INPUT===========================**************>
# seq1 = "AGGCCCTTTCT"
# seq2 = "AGGCT"
# a,b= NWSeqAlign(seq1,seq2,-2,1,-1)
# print(a)
# print(b)

#<**************============OUTPUT========================*************>

# AGGCCCTTTCT
# AGG------CT
