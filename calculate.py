import pandas as pd
data = pd.read_excel("materials.xlsx")
data["Total cost"] = data["QUANTITY"] * data["UNIT PRICE"]
print(data)
data.to_excel("materials_result.xlsx", index = False)