"""
Creating new data structure.... It should support gradients passing and computation graph
"""
class Vensor:
    def __init__(self,l):
        self.data = l[:]
    def __getitem__(self,key):
        return self.data[key]
    def __add__(self,other):
        if(type(other)==type(1)):
            res = []
            for i in range(len(self.data)):
                res.append(self.data[i]+other)
            return Vensor(res)
    def __radd__(self,other):
        if(type(other)==type(1)):
            res = []
            for i in range(len(self.data)):
                res.append(self.data[i]+other)
            return Vensor(res)
    def __mul__(self,other):
        if(type(other)==type(1)):
            res = []
            for i in range(len(self.data)):
                res.append(self.data[i]*other)
            return Vensor(res)
    def __repr__(self):
        return f"Vensor({self.data})"
