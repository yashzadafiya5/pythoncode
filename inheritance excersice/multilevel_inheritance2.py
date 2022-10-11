# 4) create multilevel inheritance example which has two class 
#     1) kg class 
#         has constructor for grams 
#         has method getKg which return kg of grams 
#     2) Ton class  inherit kg class 
#         has constructor for grams which call parent class constructor
#         has method getTon() which return Ton of grams
#     3) MetricTon class  inherit kg class 
#         has constructor for grams which call parent class constructor
#         has method getMTC() which return MetricTon of grams

class Kg:
    def __init__(self,gram):
        self.gram=gram
    def getgram(self):
        kg=self.gram/1000
        return kg
class Ton(Kg):
    def __init__(self,gram):
        super().__init__(gram)
    def getton(self):
        ton = (super().getgram() * 1.1023E-6)
        return ton
class MetricTon(Ton):
    def __init__(self,gram):
        super().__init__(gram)
    def getMetricTon(self):
        MetricTon=(super().getton() / 0.907185)
        return MetricTon
gram=int(input("enter a gram:="))
p3= MetricTon(gram)
kg=p3.getgram()
ton=p3.getton()
metricton=p3.getMetricTon()
print(f"ton is :{kg} kg")
print(f"kg is :{ton} ton")
print(f"MetricTon is :{metricton} MetricTon ")