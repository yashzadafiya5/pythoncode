# 3) create multilevel inheritance example which has two class 
#     1) KB class 
#         has constructor for bytes 
#         has method getKb which return kb of bytes 
#     2) MB class  inherit KB class 
#         has constructor for bytes which call parent class constructor
#         has method getMb() which return mb of bytes
#     3) GB class  inherit MB class 
#         has constructor for bytes which call parent class constructor
#         has method getGB() which return gb of bytes 

class Kb:
    def __init__(self,byte):
        self.byte=byte
    def getkb(self):
        kb=self.byte/1024
        return kb
class Mb(Kb):
    def __init__(self,byte):
        super().__init__(byte)
    def getmb(self):
        mb=super().getkb()/1024
        return mb
class Gb(Mb):
    def __init__(self,byte):
        super().__init__(byte)
    def getgb(self):
        gb=super().getmb()/1024
        return gb
byte=int(input("enter a kb:="))
p3=Gb(byte)
kb=p3.getkb()
mb=p3.getmb()
gb=p3.getgb()

print(f"kb is :{kb} kb")
print(f"Mb is :{mb} mb")
print(f"gb is :{gb} gb")

