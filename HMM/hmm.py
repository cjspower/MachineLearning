import tool
def main():
    A = [[0,0.3,0.4,0.3],[0,0.8,0.1,0.1],[0,0.3,0.6,0.1],[0,0.1,0.2,0.7]]
    B = [[0,0,0,0,0,0],[0.5,0.2,0.1,0.1,0.05,0.05],[0.05,0.05,0.45,0.05,0.35,0.05],[0.25,0.05,0.05,0.05,0.05,0.55]]
    X1 = [3,2,1,2,2,6,5]
    X2 = [5,1,3,4]
    X3 = [6,6,6,6,6,6,1,2,2,5]
    X4 = [1,2,6,3,3,4,1,5]
    X5 = [5,4,1,3,2,6,5,4,1,3,2]
    PI = [1,0,0,0]
    model = tool.HmmModel(A,B,PI)
    print tool.viterbi(model, X1)
    print tool.viterbi(model, X2)
    print tool.viterbi(model, X3)
    print tool.viterbi(model, X4)
    print tool.viterbi(model, X5)
    
    
if __name__ == '__main__':
    main()