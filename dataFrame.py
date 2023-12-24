import pandas as pd
data={"Name":["Bharathi","Muthu","Hari"],
    "Mark":[89,99,98]}
x=pd.DataFrame(data)
print(x.loc[0])
