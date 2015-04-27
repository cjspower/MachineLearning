import numpy as np

#just to ignore the warning generate by log(0)
np.seterr('ignore')

#create a hmm model
def HmmModel(A,B,pi,pe=0):
    "Return a hmm model based on given parameter"
    A = np.array(A)
    B = np.array(B)
    if pe==0:
        pe = np.ones(np.shape(A)[0])
    else:
        pe = np.array(pe)    
    pi = np.array(pi)
    return (A,B,pi,pe)
    
def foward(model, observation):
    
    
    
    return 0
    

def viterbi(model, observation):
    "Return a most likes hidden state sequence"
    observation = np.array(observation)
    obLength = len(observation)
    stateNum = np.shape(model[0])[0]
    alog = np.log(model[0])
    blog = np.log(model[1])
    stateSpace = range(1,stateNum+1)
    stateTable = np.zeros((obLength+1,stateNum))
    stateTable[0] = np.log(model[2])
    backTrace = []
    for count in xrange(1, obLength+1):
        currState = np.zeros((stateNum,stateNum))
        for i in xrange(0, stateNum):
            for j in xrange(0, stateNum):
                currState[i][j] = alog[i][j]+stateTable[count-1][i]
        currTrace = np.argmax(currState,0)
        currState = np.max(currState, 0) + blog[:,observation[count-1]-1]
        backTrace.append(currTrace)
        stateTable[count] = currState
    flag = np.argmax(stateTable[obLength])
    route = []
    
    for trace in reversed(backTrace):
        route.append(stateSpace[flag])
        flag = trace[flag]
    route.append(stateSpace[flag]) 
    route.reverse()
    return route