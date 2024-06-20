#->1.insert string
#->2.search string
#->3.search prefix
#->4.delete string
n=int(input())
l=set()
for i in range(n):
    n1=int(input())
    a=input()
    if(n1==1):
        l.add(a)
    elif(n1==2):
        if a in l:
            print('True')
        else:
            print('False')
    elif(n1==3):
        '''bool=True
        count=0
        for ele in l:
            if(a==ele[0:len(a)]):
                count+=1
                bool=False
        if bool:
            print('False')
        else:
            print('True',count)'''
        if l.startwith(a):
            print('True')    
    elif(n1==4):
        l.remove('word')                    

        

