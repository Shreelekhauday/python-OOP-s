#arbitary parameters(kwargs)
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key+":"+value)
student_info(name="shree",age="18",clg="bitm")