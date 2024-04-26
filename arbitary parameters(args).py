#arbitary parameters(args)
def add (*args):
    result=1
    for num in args:
        result+=num
    return result
print(add(7,5,3,9))