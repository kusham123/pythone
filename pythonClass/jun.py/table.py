# 13 * 100

# a = 13
# for i in range(1,101):
    
#     print(13 * i) 

#151
def reversedWord(str):
    res= ''
    i = 0
    n = len(str)
    
    while i < n:
        print(i)
        while i < n and str[i] == ' ':
            i+=1
            print('null string',i)
        if i >= n:
            print('stage 1')
            break
        j = i+1
        print('j',j)
        print(str[j])
        while j < n and str[j] != ' ':  
            j+=1
            print('stage2 j=',j)
        sub_str = str[i:j]
        print('sub=',sub_str)
        if len(res) == 0:
            print('step1')
            res = sub_str
        else:
            print('step2')
            res = sub_str +' '+ res
            print(res)
        i = j+1
             
    return res
             
str = " the sky is blue "
reversedWord(str)
print(reversedWord(str))
             