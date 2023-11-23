#%%Questão 1
import numpy as np
import matplotlib.pyplot as plt

MédiaPetro=0.001421
DesvpadPetro=0.022822
RetSimPetro=np.random.normal(MédiaPetro,DesvpadPetro,250)
PreçoPetro=np.zeros(251)
PreçoPetro[0]=33.57

for t in range(1,251):
    PreçoPetro[t]=RetSimPetro[t-1]*PreçoPetro[t-1]+PreçoPetro[t-1]
    
    
MédiaVale=0.001421
DesvpadVale=0.022822
RetSimVale=np.random.normal(MédiaPetro,DesvpadPetro,250)
PreçoVale=np.zeros(251)
PreçoVale[0]=33.57

for t in range(1,251):
    PreçoPetro[t]=RetSimVale[t-1]*PreçoVale[t-1]+PreçoVale[t-1]

CorrMatriz=np.corrcoef(PreçoPetro,PreçoVale)
Corr=CorrMatriz[0,1]

#%%Questão 2
import numpy as np
import matplotlib.pyplot as plt

RetClassPetro=[-0.05,0.025, 0.1, 0.175]
FreqPetro=np.array([0.02,0.45,0.51,0.02])

FreqAcumPetro= np.cumsum(FreqPetro)

RetSimPetro=np.zeros(250)
AleatPetro=np.random.uniform(0,1,250)

for t in range(0,250):
    if AleatPetro[t]<=FreqAcumPetro[0]:
        RetSimPetro[t]=RetClassPetro[0]
        
    elif AleatPetro[t]<=FreqAcumPetro[1]:
        RetSimPetro[t]=RetClassPetro[1]
        
    elif AleatPetro[t]<=FreqAcumPetro[2]:
        RetSimPetro[t]=RetClassPetro[2]
        
    else:
        RetSimPetro[t]=RetClassPetro[3]
        
PreçoPetro=np.zeros(251)
PreçoPetro[0]=33.57

for t in range(1,251):
    RetSimPetro[t-1]*PreçoPetro[t-1]+PreçoPetro[t-1]

 
