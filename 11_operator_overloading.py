class Number:
    def __init__(self, num):
        self.num = num
    
    # for add number
    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num
    
    # multiply number
    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"Deciaml Number: {self.num}"

    def __len__(self):
        return 1
n = Number(9)
print(n)    
print(len(n))

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)