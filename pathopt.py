#coded by amdad muhammed
#implementation of hungarian algo 
import math
import time

class graph():
    def __init__(self, n):
        # coloumns corresponds to return pckges and rows are delivary
        self.data = [[0 for __ in range(n)] for i in range(n)]

    def _ins(self, dpn, rpn, w):
        # indexing from 0
        self.data[dpn][rpn] = w

#collecting data here n or count is number of delivary or return points
#input points format type x y press enter to add next cordinates and so on 
def datac():
    global dlis, rlis, n
    n = int(input('count??'))

    print('delivary points!!')
    for i in range(n):
        temp = tuple(map(int, input().split()))
        dlis.append(temp)

    print('return points!!')
    for i in range(n):
        temp = tuple(map(int, input().split()))
        rlis.append(temp)


def weight(p1, p2):
    w = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return w


def opt(n,data):

    # minimum row optimization
    #data = [[82,83,69,92],[77,37,49,92],[11,69,5,86],[8,9,98,23]]
    for i in range(n):
        tmin = min(data[i])
        data[i] = [j-tmin for j in data[i]]

    # minimum coloumn optimization
    for i in range(n):
        tmin = float('inf')
        for j in range(n):
            if data[j][i] < tmin:
                tmin = data[j][i]

        for j in range(n):
            data[j][i] -= tmin

   # print(data)

    # further optimization
    ls=data.copy()
    
    
    
    
    #zlis=[]
    while True:
        
        #restricted list of rows and coloumns for marking
        rr,rc=[],[]
        asls=[['n' for __ in range(n)] for i in range(n)]
        #marking zero entries 
        for i in enumerate(ls):
            for j in enumerate(i[1]):
                if j[1]==0:
                    if (i[0] in rr) or (j[0] in rc):
                        continue 
                    asls[i[0]][j[0]]='y'
                    rr.append(i[0])
                    rc.append(j[0])
        #print(asls)
        #print(rr,rc)

        #finding rows without assighnment 'y'
        rows_marked=[]
        for i in range(n):
            if i not in rr:
                rows_marked.append(i)
       
       
        columns_marked=[]
        while True:
            rpt=0
            #marking coloumns
            for i in rows_marked:
                for j in enumerate(ls[i]):
                    if j[1]==0:
                        if not j[0] in columns_marked:
                            columns_marked.append(j[0])
                            rpt+=1
                    
      #      print(columns_marked)
        
            #marking rows
            for i in columns_marked:
                for j in range(n):
                    if asls[j][i]=='y':
                        if not j in rows_marked:
                            rows_marked.append(j)
                            rpt+=1

            if rpt==0:
                break

     #   print(rows_marked,columns_marked)
        rows_selected=[]
        for i in range(n):
            if i not in rows_marked:
                rows_selected.append(i)
        columns_selected=columns_marked
      #  print('ssdd',rows_selected,columns_selected)     
        if len(columns_selected)+len(rows_selected)>=n:    
            break
        else:
            tmin=float('inf')
            for i in range(n):
                if i in rows_selected:
                    continue
                for j in range(n):
                    if j in columns_selected:
                        continue
                    if ls[i][j]<tmin:
                        tmin=ls[i][j]
     #       print(tmin)
            for i in range(n):
                for j in range(n):
                    if (i in rows_selected) and (j in columns_selected):
                        ls[i][j]+=tmin
                        continue
                    if (j in columns_selected) or (i in rows_selected):
                        continue
                    else:
                        ls[i][j]-=tmin           
                    
    #print(ls)     

    #extracting the best combination
    ordlist,rr,rc=[],[],[]  
    for i in range(n):
        for j in range(n):
            if ls[i][j]==0:
                if (i not in rr) and (j not in rc):
                    ordlist.append((i,j))
                    rr.append(i)
                    rc.append(j)
                    break
    if len(ordlist)==n:
        return(ordlist)
    else:
        ordlist,rr,rc=[],[],[]  
        rcount={}
        ccount={}
        for i in range(n):
            for j in range(n):
                if ls[i][j]==0:
                    rcount[i]=rcount.get(i,0)+1
                    ccount[j]=ccount.get(j,0)+1
        print(rcount,ccount)
        for i in rcount.keys():
            if rcount[i]==1:
                c=ls[i].index(0)
                rr.append(i)
                rc.append(c)
                ordlist.append((i,c))
        for i in ccount.keys():
            if ccount[i]==1:
                for j in range(n):
                    if ls[j][i]==0:  
                        ordlist.append((j,i))      
                        rr.append(j)
                        rc.append(i)
                        break
        print(rr,rc)
        for i in range(n):
            for j in range(n):
                if ls[i][j]==0:
                    if (i not in rr) and (j not in rc):
                        ordlist.append((i,j))
                        rr.append(i)
                        rc.append(j)
                        break       
        
        return ordlist

def main():
    global dlis, rlis, n
    datac()
    gr = graph(n)
    for i in enumerate(dlis):
        for j in enumerate(rlis):
            gr._ins(i[0], j[0], (weight(i[1], j[1])))

    # implementing hungarian algo

    ordlist=opt(n,gr.data)
   # print(ordlist)
    finallist=[]
    for i in ordlist:
        finallist.append('d '+str(i[0]))
        finallist.append('r '+str(i[1]))
    print(finallist)    


if __name__ == "__main__":
    ti=time.time()
    dlis, rlis, n = [], [], int()
    main()
    tf=time.time()
    print('runtime',tf-ti)
    print('DONE')