#APS Finanças - Empresa : Camil (CAML3.SA)
#Grupo
"""
Beatriz Emi Ueda
Beatriz Fernandes da Silva
Gabriela Abib
Hicham Munir Tayfour
Júlia de Aquino Rocha
Raynnara Silva de Freitas
"""
#%%Importação das Bibliotecas
import pandas as pd
import matplotlib.pyplot as fig 
import numpy as np
#%%Importação dos dados 
bp=pd.read_excel('CAML3.xlsx', sheet_name='BP')
dre=pd.read_excel('CAML3.xlsx', sheet_name='DRE')
dfc=pd.read_excel('CAML3.xlsx', sheet_name='DFC')
fcx=pd.read_excel('CAML3.xlsx',sheet_name='FCx')
#%%Gráfico dos Projeções
receita_2018=dre.loc[9, 'Unnamed: 2']
receita_2019=dre.loc[9, 'Unnamed: 3']
receita_2020=dre.loc[9, 'Unnamed: 4']
receita_2021=dre.loc[9, 'Unnamed: 5']
receita_2022=dre.loc[9, 'Unnamed: 6']
receitas=np.array([receita_2018,receita_2019,receita_2020,receita_2021,receita_2022])
taxas_variacao = np.empty(5)
i=0
for i in range(1, 5):
    taxa_var = (receitas[i] / receitas[i - 1]) - 1
    taxas_variacao[i] = taxa_var
taxas_variacao[0]=np.nan
taxas_variacao=taxas_variacao*100
anos = np.array([2018, 2019, 2020, 2021, 2022])
fig.plot(anos, taxas_variacao, marker='o', linestyle='-')
fig.xlabel('Ano')
fig.ylabel('Taxa de Variação em %')
fig.title('Taxa de Variação da Receita',fontsize=20)
fig.grid(True)  
fig.show()
"""Pelo fato da taxa de variação entre 2019 e 2020 ter dado um valor anormal, 
desconsideraremos seu valor para calcular uma média de crescimento para a receita da empresa"""
media_crescimento=(taxas_variacao[1]+taxas_variacao[3]+taxas_variacao[4])/3

#%%Cálculo dos G's
"Lucros Líquidos"
lucro_2018=dre.loc[51, 'Unnamed: 2']
lucro_2019=dre.loc[51, 'Unnamed: 3']
lucro_2020=dre.loc[51, 'Unnamed: 4']
lucro_2021=dre.loc[51, 'Unnamed: 5']
lucro_2022=dre.loc[51, 'Unnamed: 6']
lucros_liquidos=np.array([lucro_2018,lucro_2019,lucro_2020,lucro_2021,lucro_2022])
"Dividendos Pagos"
dividendo_2018=-(dfc.loc[29, 2018])
dividendo_2019=-(dfc.loc[29, 2019])
dividendo_2020=-(dfc.loc[29, 2020])
dividendo_2021=-(dfc.loc[29, 2021])
dividendo_2022=-(dfc.loc[29, 2022])
dividendos=np.array([dividendo_2018,dividendo_2019,dividendo_2020,dividendo_2021,dividendo_2022])
"Taxa de Payout de Dividendos"
indice_payout=np.empty(5)
i=0
for i in range(0,5):
    payout=dividendos[i]/lucros_liquidos[i]
    indice_payout[i]=payout
Payout_med=np.mean(indice_payout)
"R.O.A"
lucro_2018=dre.loc[51, 'Unnamed: 2']
lucro_2019=dre.loc[51, 'Unnamed: 3']
lucro_2020=dre.loc[51, 'Unnamed: 4']
lucro_2021=dre.loc[51, 'Unnamed: 5']
lucro_2022=dre.loc[51, 'Unnamed: 6']
lucros_liquidos=np.array([lucro_2018,lucro_2019,lucro_2020,lucro_2021,lucro_2022])

ativo_2018=bp.loc[34,'Unnamed: 3']
ativo_2019=bp.loc[34,'Unnamed: 4']
ativo_2020=bp.loc[34,'Unnamed: 5']
ativo_2021=bp.loc[34,'Unnamed: 6']
ativo_2022=bp.loc[34,'Unnamed: 7']
ativos_totais=np.array([ativo_2018,ativo_2019,ativo_2020,ativo_2021,ativo_2022])
roa=np.empty(5)
i=0
for i in range(0,5):
    ROA=lucros_liquidos[i]/ativos_totais[i]
    roa[i]=ROA
ROA_med=np.mean(roa)
"R.O.E"
lucro_2018=dre.loc[51, 'Unnamed: 2']
lucro_2019=dre.loc[51, 'Unnamed: 3']
lucro_2020=dre.loc[51, 'Unnamed: 4']
lucro_2021=dre.loc[51, 'Unnamed: 5']
lucro_2022=dre.loc[51, 'Unnamed: 6']
lucros_liquidos=np.array([lucro_2018,lucro_2019,lucro_2020,lucro_2021,lucro_2022])

pl_2018=bp.loc[64,'Unnamed: 3']
pl_2019=bp.loc[64,'Unnamed: 4']
pl_2020=bp.loc[64,'Unnamed: 5']
pl_2021=bp.loc[64,'Unnamed: 6']
pl_2022=bp.loc[64,'Unnamed: 7']
pls=np.array([pl_2018,pl_2019,pl_2020,pl_2021,pl_2022])
roe=np.empty(5)
i=0
for i in range(0,5):
    ROE=lucros_liquidos[i]/pls[i]
    roe[i]=ROE
ROE_med=np.mean(roe)

"G_interno"
g_int=(ROA_med*(1-Payout_med))/(1-ROA_med*(1-Payout_med))

"G_sustentável"
g_sus=(ROE_med*(1-Payout_med))/(1-ROE_med*(1-Payout_med))
#%%Gráfico das Projeção

"Gráfico da Projeção do Balanço Patrimonial (Ativo, Passivo e PL)"
ativo_2023E=bp.loc[34,'Unnamed: 8']
ativo_2024E=bp.loc[34,'Unnamed: 9']
ativo_2025E=bp.loc[34,'Unnamed: 10']
ativo_2026E=bp.loc[34,'Unnamed: 11']
ativo_2027E=bp.loc[34,'Unnamed: 12']
ativos_projetados=np.array([ativo_2023E,ativo_2024E,ativo_2025E,ativo_2026E,ativo_2027E])

passivo_2023E=bp.loc[36,'Unnamed: 8']+bp.loc[55,'Unnamed: 8']
passivo_2024E=bp.loc[36,'Unnamed: 9']+bp.loc[55,'Unnamed: 9']
passivo_2025E=bp.loc[36,'Unnamed: 10']+bp.loc[55,'Unnamed: 10']
passivo_2026E=bp.loc[36,'Unnamed: 11']+bp.loc[55,'Unnamed: 11']
passivo_2027E=bp.loc[36,'Unnamed: 12']+bp.loc[55,'Unnamed: 12']
passivos_projetados=np.array([passivo_2023E,passivo_2024E,passivo_2025E,passivo_2026E,passivo_2027E])

pl_2023E=bp.loc[64,'Unnamed: 8']
pl_2024E=bp.loc[64,'Unnamed: 9']
pl_2025E=bp.loc[64,'Unnamed: 10']
pl_2026E=bp.loc[64,'Unnamed: 11']
pl_2027E=bp.loc[64,'Unnamed: 12']
pl_projetados=np.array([pl_2023E,pl_2024E,pl_2025E,pl_2026E,pl_2027E])

anos_E = np.array([2023, 2024, 2025, 2026, 2027])
fig.figure(figsize=(10, 6))
fig.plot(anos_E, ativos_projetados, label='Ativos', marker='o', linestyle='-')
fig.plot(anos_E, passivos_projetados, label='Passivos', marker='o', linestyle='-')
fig.plot(anos_E, pl_projetados, label='Patrimônio Líquido', marker='o', linestyle='-')
fig.xlabel('Ano')
fig.ylabel('Valor')
fig.title('Projeção Financeira',fontsize=20)
fig.legend()
fig.grid(True)  
fig.show()

"Gráfico da Projeção da Receita e do Lucro Líquido"
receita_2023E=dre.loc[9, 'Unnamed: 7']
receita_2024E=dre.loc[9, 'Unnamed: 8']
receita_2025E=dre.loc[9, 'Unnamed: 9']
receita_2026E=dre.loc[9, 'Unnamed: 10']
receita_2027E=dre.loc[9, 'Unnamed: 11']
receita_projetada=np.array([receita_2023E,receita_2024E,receita_2025E,receita_2026E,receita_2027E])

lucro_2023E=dre.loc[51, 'Unnamed: 7']
lucro_2024E=dre.loc[51, 'Unnamed: 8']
lucro_2025E=dre.loc[51, 'Unnamed: 9']
lucro_2026E=dre.loc[51, 'Unnamed: 10']
lucro_2027E=dre.loc[51, 'Unnamed: 11']
lucro_projetado=np.array([lucro_2023E,lucro_2024E,lucro_2025E,lucro_2026E,lucro_2027E])

fig.figure()
fig.plot(anos_E, receita_projetada, label='Receita', marker='o', linestyle='-')
fig.plot(anos_E, lucro_projetado, label='Lucro Líquido', marker='o', linestyle='-')
fig.xlabel('Ano')
fig.ylabel('Valor')
fig.title('Projeção Financeira da DRE',fontsize=20)
fig.legend()
fig.grid(True)  
fig.show()

"Gráfico da Projeção dos Fluxos de Caixa"
fca_2023E=fcx.loc[26,'Unnamed: 8']
fca_2024E=fcx.loc[26,'Unnamed: 9']
fca_2025E=fcx.loc[26,'Unnamed: 10']
fca_2026E=fcx.loc[26,'Unnamed: 11']
fca_2027E=fcx.loc[26,'Unnamed: 12']
fca_projetado=np.array([fca_2023E,fca_2024E,fca_2025E,fca_2026E,fca_2027E])

fcs_2023E=fcx.loc[36,'Unnamed: 8']
fcs_2024E=fcx.loc[36,'Unnamed: 9']
fcs_2025E=fcx.loc[36,'Unnamed: 10']
fcs_2026E=fcx.loc[36,'Unnamed: 11']
fcs_2027E=fcx.loc[36,'Unnamed: 12']
fcs_projetado=np.array([fcs_2023E,fcs_2024E,fcs_2025E,fcs_2026E,fcs_2027E])

fcb_2023E=fcx.loc[50,'Unnamed: 8']
fcb_2024E=fcx.loc[50,'Unnamed: 9']
fcb_2025E=fcx.loc[50,'Unnamed: 10']
fcb_2026E=fcx.loc[50,'Unnamed: 11']
fcb_2027E=fcx.loc[50,'Unnamed: 12']
fcb_projetado=np.array([fcb_2023E,fcb_2024E,fcb_2025E,fcb_2026E,fcb_2027E])

fig.figure()
fig.plot(anos_E, fca_projetado, label='FC(A)', marker='o', linestyle='-')
fig.plot(anos_E, fcs_projetado, label='FC(S)', marker='o', linestyle='-')
fig.plot(anos_E, fcb_projetado, label='FC(B)', marker='o', linestyle='-')
fig.xlabel('Ano')
fig.ylabel('Valor')
fig.title('Projeção Financeira dos Fluxos de Caixa',fontsize=20)
fig.legend()
fig.grid(True)  
fig.show()

"Gráfico da NAF"
NAF_2023=bp.loc[162,'Unnamed: 8']
NAF_2024=bp.loc[162,'Unnamed: 9']
NAF_2025=bp.loc[162,'Unnamed: 10']
NAF_2026=bp.loc[162,'Unnamed: 11']
NAF_2027=bp.loc[162,'Unnamed: 12']
naf_projetadas=np.array([NAF_2023,NAF_2024,NAF_2025,NAF_2026,NAF_2027])

fig.figure(figsize=(10, 6))
fig.plot(anos_E, naf_projetadas, label='NAFs', marker='o', linestyle='-')
fig.xlabel('Ano')
fig.ylabel('Valor')
fig.title('Projeção da Necessidade de Aporte Financeiro (NAF)',fontsize=20)
fig.legend()
fig.grid(True)  
fig.show()

"Gráfico da Comparção da Receita com sua Projeção"
receita_2018=dre.loc[9, 'Unnamed: 2']
receita_2019=dre.loc[9, 'Unnamed: 3']
receita_2020=dre.loc[9, 'Unnamed: 4']
receita_2021=dre.loc[9, 'Unnamed: 5']
receita_2022=dre.loc[9, 'Unnamed: 6']
receitas=np.array([receita_2018,receita_2019,receita_2020,receita_2021,receita_2022])
receita_2023E=dre.loc[9, 'Unnamed: 7']
receita_2024E=dre.loc[9, 'Unnamed: 8']
receita_2025E=dre.loc[9, 'Unnamed: 9']
receita_2026E=dre.loc[9, 'Unnamed: 10']
receita_2027E=dre.loc[9, 'Unnamed: 11']
receita_projetada=np.array([receita_2023E,receita_2024E,receita_2025E,receita_2026E,receita_2027E])
anos_T = np.array([2018,2019,2020,2021,2022,2023,2024,2025,2026,2027])
fig.figure(figsize=(10, 6))
fig.plot(anos_T[:5], receitas, label='Receita', marker='o', linestyle='-')
fig.plot(anos_T[5:], receita_projetada, label='Receita Projetada', marker='o', linestyle='-')
fig.xlabel('Ano')
fig.ylabel('Valor')
fig.title('Comparação das Receitas', fontsize=20)
fig.legend()
fig.grid(True)
fig.show()


#%%