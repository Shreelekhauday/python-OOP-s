#arbitary parameters
def multiply (*args):
    result=1
    for num in args:
        result*=num
    return result
print(multiply(7,5,3,9))