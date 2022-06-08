array=[5,1,22,25,6,-1,8,10]
sequence=[1,6,-1,10]

def isSequence(array,sequence):
    indexes=[]
    for i in range(len(sequence)):
        seq=sequence[i]
        print(seq)
        if seq in array:
           
            indexes+=[array.index(seq)]
        else:
            return False
    return indexes

isSequence(array,sequence) 