# 2 create single level inheritance example which has two class 
#     1) KB class 
#         has constructor for bytes 
#         has method getKb which return kb of bytes 
#     2) MB class  inherit KB class 
#         has constructor for bytes which call parent class constructor
#         has method getMb() which return mb of bytes 

class Kb:
    def __init__(self,kb):
        self.kb=kb
    def getbyte(self):
        byte=self.kb*1024
        print(f"kb:{self.kb} convert byte is :{byte}")
        return byte
class Mb(Kb):
    def getmb(self):
        super().__init__(kb)
        mb= (super().getbyte())/(1024*1024)
        print(f"byte:{super().getbyte()} convert Mb is :{mb}")
        return mb
kb=int(input("enter a kb"))        
s1=Mb(Kb)
s1.getmb()