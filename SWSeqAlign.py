def SWSeqAlign(seq1,seq2,gap_score=-2,match_score=1,mismatch_score=-1):
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
    k = l * gap_score
    if k < 0:
      k = 0
    matrix[0][l] = k
  for m in range(1,len(seq1)+1):
    k = l * gap_score
    if k < 0:
      k = 0
    matrix[m][0] = k



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
      if diag<0:
        diag = 0
      if up < 0:
        up = 0
      if left<0:
        left = 0 
      matrix[row][column] = max(up,left,diag)

  #<=========Backtracing===========>
  
  A,B = Backtracing(seq1,seq2, matrix, gap_score,match_score,mismatch_score)

  return matrix,A,B
      


#<========Function for Backtracing=========>
def Backtracing(seq_2,seq_1,matrix,gap,match_score,mismatch_score):
  p = 0
  l=0
  for i in range(len(matrix)):
    k = max(matrix[i])
    if k > p :
      p = k 
      l = i
  j = 0
  for s in range(len(matrix[p])):
    if p == matrix[l][s]:
      j = s 
  AlignmentA = ""
  AlignmentB = ""
  d = gap
  row = l
  col = j

  while row>0 and col>0:
    score = matrix[row][col]
    scoreDiag = matrix[row-1][col-1]
    if score > scoreDiag:
      AlignmentB = seq_1[col-1] + AlignmentB
      row-=1
      col-=1
    else:
      break

  #Alignment
  seq_2 = "".join(seq_2)
  seq4 = seq_2.find(AlignmentB)
  seqk = []
  for i in range(0,len(seq_2)-len(AlignmentB)+1):
    if i == seq4:
      seqk.append(AlignmentB)
    else:
      seqk.append("-")
    if len(seqk)+1 >=len(seq_2):
      break
  seqk = "".join(seqk)



  return seq_2,seqk
