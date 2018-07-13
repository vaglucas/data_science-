import pandas as pd

heads = ('NO_MUNICIPIO_RESIDENCIA','NU_NOTA_REDACAO','TP_ESCOLA','SG_UF_RESIDENCIA')

enem =pd.read_csv('microdados_enem_2016.csv',names=None,header =0,sep=";", encoding ="latin-1",nrows=300000)
enemDf = pd.DataFrame(enem,columns=heads)
#cp = enemDf.query('NU_NOTA_REDACAO>500 ').copy()
#query('NO_MUNICIPIO_RESIDENCIA == "Joaçaba" & SG_UF_RESIDENCIA == "SC" & NU_NOTA_REDACAO >700 ').copy()
#enemDf.query('NU_NOTA_REDACAO > 950 ').copy()
#enemDf.query('NO_MUNICIPIO_NASCIMENTO == "Catanduvas"  ').copy()
print((enemDf.query('NU_NOTA_REDACAO>500 ').size+enemDf.query('NU_NOTA_REDACAO<500 ').size))



print("fim")
