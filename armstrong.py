num=int(input('enter the number'))
def is_armstrong(num):
    num_digits=len(str(num))
    armstrong_sum=0
    temp=num
    while temp>0:
        digit=temp%10
        armstrong_sum+=digit**num_digits
        temp//=10
    return num==armstrong_sum
print(is_armstrong(num))