class BankAccount:
    def __init__(self,deposit,withdrawl,bankbalance):
        self.a=deposit
        self.b=withdrawl
        self.c=bankbalance
    def simplebankacc(self):
        return self.a,self.b,self.c
        return "choose one option"
obj=BankAccount("deposit","withdrawl","bankbalnce")
res=obj.simplebankacc()
print(res)
