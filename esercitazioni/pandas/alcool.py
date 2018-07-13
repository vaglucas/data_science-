import pandas as pd
import numpy as np
names_ = ("region","division","state")
alcoo2009 =pd.read_csv("niaaa.csv",
                        header=0,
                        names=names_)
state2reg_series = alcoo2009.ffill().set_index("state")["region"]
print(state2reg_series.head())


alcoo2009.index.name="State"
alcoo2009.name="drinks"


print(alcoo2009)
