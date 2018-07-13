
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


# Ora che abbiamo importato tutto quello che ci serve chiediamo a Pandas di leggere i nostri dati attraverso la read fwf function.

# In[2]:

dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]


# Quello che abbiamo fatto è trasformare il nostro file txt in struttura 2d di colonne e righe. Quello che contengono sono i valore medi di un certo numero di specie animali riguardo peso del cervello e peso del corpo.  
# In questo modo possiamo sistemare i pesi del cervello nel nostro asse X e i pesi del corpo su Y. 
# Ecco a voi il grafico. 

# In[3]:

get_ipython().magic(u'matplotlib notebook')

plt.xlabel("brain")
plt.ylabel("body")
plt.scatter(x_values, y_values)
plt.show()


# Abbiamo semplicemente chiesto a matplotlib di creare un grafico in cui viene mostrato il nostro dataset. 
# Già ad occhio possiamo riscontrare una discreta correlazione. 
# Il nostro obiettivo quindi è che dato un nuovo peso saremo capaci di predire quale sia la taglia del suo cervello. 
# In che modo? Passiamo un attimo alle cose formali.
# Abbiamo una variabile indipendete che è X e una variabile dipendente che è Y. Quello che dobbiamo fare è trovare la relazione che intercorre fra di loro appunto utilizzando la Linear Regression. 
# Letteralmente dobbiamo trovare la linea che maggiormente si adatta ai nostri dati. Di cosa abbiamo bisogno? Di una semplice equazione.
# Y = mx + b. 
# In cui b è l'intercetta ed mx la sua inclinazione. 
# Non ci resta che applicarla al nostro grafico. 
# 

# In[9]:

body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)
body_reg_pred = body_reg.predict(x_values)


# Siamo usciti abbastanza indenni dalla parte matematica. Vediamo ora, chiamando il grafico, la nostra linea che abbiamo generato poco fa. 

# In[13]:

get_ipython().magic(u'matplotlib notebook')

plt.xlabel("brain")
plt.ylabel("body")
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg_pred, color = 'green', linewidth = 3)
plt.show()