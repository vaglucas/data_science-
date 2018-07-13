import pandas as pd
import numpy as np
print("===============================================PANDAS=====================================================================")
#inflation = pd.Series((2.2,3.4,2.8,1.6,2.3,2.7,3.4,3.2,2.8,3.8,-0.4,1.6,3.2,2.1,1.5,1.5))
#print(inflation)
#print(inflation.index)#index.values
#print(inflation.values)
#inflation.values[-1] = 1.6
#inflation.values[15] = 1.6

inflation = pd.Series({1999 : 2.2,2000 : 3.4,2001 : 2.8,2002 : 1.6,2003 : 2.3,2004 : 2.7,2005 : 3.4,2006 : 3.2,2007 : 3.2,2008 : 2.8,2009 : 3.8,2010 : -0.4,2011 : 1.6,2012 : 3.2,2013 : 2.1 , 2014 : 1.6,2015 : np.nan})



inflation.index = pd.Index(range(1999,2016))
inflation[2015] = np.nan

inflation.index.name = "Year"
inflation.name = "%"

inflation.head()
inglation.tail()

print(inflation)
