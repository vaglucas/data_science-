import numpy as np
import matplotlib
import matplotlib.pyplot as plt

dirt =np.arange(-1,3,0.2)

whos_dirt = dirt <0
#print(dirt)
#print(whos_dirt)

dirt[whos_dirt]=0

#print(dirt)

linear = np.arange(-1,2,0.2)
#print(linear)
linear = (linear <=0.5)&(linear>=-0.5)
#rint(linear),


a = np.arange(4)
b = np.arange(1,5)
#print(a," + ",b)
c = a+b
#print(c)
a = a.reshape(2,2)
b = b.reshape(2,2)

sap = np.array(["MMM","ABT","ABBV","ACN","ACE","ATVI","ADBE","ADT"])
sap2d = sap.reshape(2,4)
sap3d = sap.reshape(2,2,2)
"""
multuply, add negative exp log sqrt
sin cos hypot
bitwise_and legt_shift
less, logical_not, equal,
maximum, minimun"""
c = np.multiply(a,b)
print(c)
print("==============EYE==============")
noise = np.eye(4)+ 0.01 * np.random.random([4, 4])
noise = np.round(noise,2)
print(noise)

stocks = np.array([140.49,0.97,40.68,41.53,55.7,57.21,98.2,99.19,109.96,111.47,35.71,36.27,87.85,89.11,30.22,30.91])

stocks = stocks.reshape(int(len(stocks)/2),2).T
print(stocks)
fall = np.greater(stocks[0],stocks[1])
print(sap[fall])

stocks[1,0]= np.nan
print("IS A NAN")
print(np.isnan(stocks))
stocks[np.isnan(stocks)]=0
print(stocks)
"""
where(c,a,b)
funzione di operatori ternario,
c booleando, a, b array
mp.nonzero
indici di tutti i elementi non zero
print(a)
anonzero = np.nonzero(a)
,print(anonzero)
"""

changes = np.where(np.abs(stocks[1]-stocks[0])>1.0,stocks[1]-stocks[0],0)
print(sap[np.nonzero(changes)])
print(sap[stocks[1]-stocks[0]>1.00])


"""
calcolo dell interesse semplice e composto per 30 anni con un tasso di interesse del 3.75%
"""
RATE = .0375
TERM = 30
simple = (RATE*np.ones(TERM)).cumsum()
compund = ((1+RATE)*np.ones(TERM)).cumprod()-1
print("simple: ", simple," composto: ",compund)
"""
np.save("sap.npy",sap)
sapcopy = np.load("sap.npy",mmap_mode="r")
print(sapcopy)
"""

"""
le costanti difinisco le proprieta
il segnale il rumore e lo "strumento"
"""
SIG_AMPLITUDE = 10; SIG_OFFSET = 2; SIG_PERIOD = 100
NOISE_AMPLITUTDE = 3
N_sample = 5 * SIG_PERIOD
INSTRUMENT_RANGE = 9

#construisce un'onda sinusoidale e le aggiunge del rumore casuale
times = np.arange(N_sample).astype(float)
signal = SIG_AMPLITUDE *np.sin(2*np.pi*times/SIG_PERIOD)+SIG_OFFSET
noise = NOISE_AMPLITUTDE +np.random.normal(size=N_sample)
signal += noise

#tronca i picchi che cadono all'esterno del range dello strumento
signal[signal>INSTRUMENT_RANGE]=INSTRUMENT_RANGE
signal[signal< -INSTRUMENT_RANGE]-INSTRUMENT_RANGE

matplotlib.style.use("ggplot")
plt.plot(times,signal)
plt.title("Synthetic sine wave signal")
plt.ylabel("Signal+noise")
plt.xlabel("Time")
plt.ylim(ymin = -SIG_AMPLITUDE,ymax=SIG_AMPLITUDE)
plt.show()
