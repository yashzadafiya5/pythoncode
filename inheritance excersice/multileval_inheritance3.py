class Foot:
    def __init__(self,inch):
        self.inch=inch
    def foot(self):
        foot=self.inch/12
        return foot
class Meter(Foot):
    def __init__(self,inch):
        super().__init__(inch)
    def meter(self):
        meter=super().foot()/3.281
        return meter
class Km(Meter):
    def __init__(self, inch):
        super().__init__(inch)
    def km(self):
        km=super().meter()/1000
        return km
    
inch=int(input("enter a number:"))

a=Km(inch)
foot=a.foot()
meter=a.meter()
km=a.km()

print(f"foot is :{foot}foot")
print(f"meter is :{meter}meter")
print(f"km is :{km}km")