#Python 3
   
word = input()
n = int(input())
n=n-1

for i in range(len(word)):
    n = n+1
    count = 0
    if (n != len(word)):
        a =(word[i:n])
        for i in range(len(a)):
            if a[i] in ('a', 'e', 'i', 'o', 'u'):
                count += 1        
        print(count,a)
    else:
        break
    
