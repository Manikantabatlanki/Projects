class Bank:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def info(self):
        print(f'acount holders name is {self.name} and his location is {self.location}')

obj=Bank('manikanta','hyderabad')
res=obj.info()
print(res)
