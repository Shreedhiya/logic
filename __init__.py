class vech:
    name="sandy"
    def __init__(self,age):
        print("constructor")
        print(age)
v=vech(10)
setattr(v,'name','sindhu')
print(getattr(v,'name'))
