# 46. Defang IP Address 


def defangIPaddr(address):
   address = address.split(".")
   return "[.]".join(address)
print("example:192.168.4.1")
ipaddress=input("enter your ip address :")
print(defangIPaddr(ipaddress))