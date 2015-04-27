import numpy as np

#just to ignore the warning generate by log(0)
np.seterr('ignore')

#create a hmm model
def HmmModel(A,B,pi,pe=0):
    "Return a hmm model based on given parameter"
    A = np.array(A).astype(float)
    B = np.array(B).astype(float)
    if pe==0:
        pe = np.ones(np.shape(A)[0]).astype(float)
    else:
        pe = np.array(pe).astype(float)   
    pi = np.array(pi).astype(float)
    return (A,B,pi,pe)

def normalize(A):
    s = sum(A)
    A = A/s
    return (A,np.log(s))  
   
    
def forward(model, observation):
    "Return the log probability alpha_i T"
    obLength = len(observation)
    stateNum = np.shape(model[0])[0]
    alphaTable = np.zeros((obLength,stateNum))
    temp = normalize(model[2]*model[1][:,observation[0]-1])
    alphaTable[0] = temp[0]
    x = temp[1]
    for t in xrange(1, obLength):
        temp = normalize(np.dot(alphaTable[t-1],model[0])*model[1][:,observation[t]-1])
        alphaTable[t] = temp[0]
        x = x + temp[1]
    return (alphaTable, x)

def backward(model, observation):
    obLength = len(observation)
    stateNum = np.shape(model[0])[0]
    betaTable = np.zeros((obLength,stateNum))
    
    

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
    route.reverse()
    return route