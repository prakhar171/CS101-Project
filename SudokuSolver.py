#CS101 Project
#Sudoku Solver USing Backtracking

import sys, os

'''
The standard input textfile will contain an integer N in the first line, denoting the number of sudokus to be solved.
The next 9*N lines will contain 9 integers each, each line denoting a row of a sudoku. 
The integers should be between 0 to 9, with 0 denoting an unfilled cell of sudoku.
'''
#Checks if any of the constraints are violated.
def isValid(sudo, ind):
    #Checks for row.
    for x in range(9):
        if sudo[ind[0]][x][0]==sudo[ind[0]][ind[1]][0] and x!=ind[1]:
            return False
    
    #Checks for column.
    for x in range(9):
        if sudo[x][ind[1]][0]==sudo[ind[0]][ind[1]][0] and x!=ind[0]:
            return False
    
    #Checks for 3x3 box.
    x=3*(ind[0]//3)
    y=3*(ind[1]//3)
    for i in range(x, x+3):
        for j in range(y, y+3):
            if sudo[i][j][0]==sudo[ind[0]][ind[1]][0] and [i, j]!=ind:
                return False
    
    return True
    

def sudokuSolver(sudo):
    
    #Initialization
    ind=None
    for x in range(81):
        if sudo[x//9][x%9][0]==0:
            ind=[x//9, x%9]
            break
    
    if ind==None:
        return sudo
    
    while True:
        if sudo[ind[0]][ind[1]][0]<9:
            sudo[ind[0]][ind[1]][0]+=1
            if isValid(sudo, ind):
                ctr=ind[0]*9+ind[1]+1
                ind=None
                for x in range(ctr, 81):
                    if sudo[x//9][x%9][0]==0:
                        ind=[x//9, x%9]
                        break
        else:
            
            sudo[ind[0]][ind[1]][0]=0 
            ctr=ind[0]*9+ind[1]-1
            ind=None       
            for x in range(ctr, -1, -1):
                if sudo[x//9][x%9][1]==False:
                    ind=[x//9, x%9]
                    break
            
        if ind==None:
            return sudo
        
             
    

filename=''
try:
    filename=sys.argv[1]
except:
    while filename=='' or not os.path.exists(filename):
        filename=input("Enter a valid input text filename:")
        

#Reading Input from the text file.
with open(filename, 'r') as ifile:
    inp=ifile.readlines()


wfile=open('out.txt', 'w')

ctr=0
N=int(inp[ctr])
ctr+=1

#Solving N Sudokus.
for x in range(N):
    sudo=[]
    for y in range(9):
        adder=[]
        temp=list(map(int, inp[ctr].split()))
        ctr+=1
        for num in temp:
            if num==0:
                adder.append([num, False])
            else:
                adder.append([num, True])
        sudo.append(adder)
                
    wfile.write("Solution to Case #"+str(x+1)+": \n")
    sudo=sudokuSolver(sudo)
    
    for y in sudo:
        res=''
        for values in y:
            res+=str(values[0])
            res+=' '
        wfile.write(res[:-1]+"\n")
    print('Completed Test Case '+str(x+1)+'!!\n')
    
        
    
        
    
        
    
    
