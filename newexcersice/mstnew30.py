# 30. Price Elasticity of Demand using Python 
import pandas as pd

# data=pd.DataFrame({"Demand":[500,1000,400,1200],"Price":[50000,10000,4000,12000]})
# print(data)


# data["% Change in Demand"] = data["Demand"].pct_change()
# data["% Change in Price"] = data["Price"].pct_change()
# print(data)

data1=pd.DataFrame({"Demand":[500,1000,400,1200],"Price":[50000,10000,4000,12000]})
data2=pd.DataFrame({"Demand":[200,500,800,900],"Price":[40000,10000,2000,6000]})

i=((data1["Demand"]- data2["Demand"])/(data1["Demand"]+ data2["Demand"]))/((data1["Price"]- data2["Price"])/
(data1["Price"]+ data2["Price"]))
print(i)
