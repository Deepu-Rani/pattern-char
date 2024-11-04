n=5
for i in range(1,n+1):
    k=65
    for j in range(1,n+1):
        if(i+j>=n+1):
            print(chr(k),end=' ')
            k+=1
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if(i>j):
            k= k-1
            print(chr(k-1),end=' ')
        else:
            print(' ',end=' ')
    print()


OUTPUT:

        A           
      A B A         
    A B C B A       
  A B C D C B A     
A B C D E D C B A   
