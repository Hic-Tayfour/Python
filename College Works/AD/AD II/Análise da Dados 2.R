#Alunos 

"Beatriz Emi Ueda (beatrizeu@al.insper.edu.br)
Beatriz Fernandes da Silva (beatrizfs1@al.insper.edu.br)
Gabriela Abib (gabrielaa6@al.insper.edu.br)
Hicham Munir Tayfour (hichamt@al.insper.edu.br)
Raynnara Silva de Freitas Gurgel (raynnarasf@al.insper.edu.br)"

#Importação da Base de Dados
library(readxl)
dados <- read_excel("Internacoes_causas_externas(1).xlsx")

#Letra A)----
#Estatísticas Básicas Dos anos
med_2021=mean(dados$`Ano 2021`)
med_2021
med_2022=mean(dados$`Ano 2022`)
med_2022
desv_2021=sd(dados$`Ano 2021`)
desv_2021
desv_2022=sd(dados$`Ano 2022`)
desv_2022

#Letra B)----
#Intervalo de Confiância dos anos
tc=abs(qt(0.025,26))
tc
e_2021=tc*desv_2021/sqrt(n)
e_2021
li_2021=med_2021-e_2021
li_2021
ls_2021=med_2021+e_2021
ls_2021

e_2022=tc*desv_2022/sqrt(n)
e_2022
li_2022=med_2022-e_2022
li_2022
ls_2022=med_2022+e_2022
ls_2022

q2=qchisq(0.975,26)
q2
q1=qchisq(0.025,26)
q1

li_var_2021=(27-1)*(desv_2021^2)/q2
li_var_2021
li_desv_2021=sqrt(li_var_2021)
li_desv_2021
ls_var_2021=(27-1)*(desv_2021^2)/q1
ls_var_2021
ls_desv_2021=sqrt(ls_var_2021)
ls_desv_2021

li_var_2022=(27-1)*(desv_2022^2)/q2
li_var_2022
li_desv_2022=sqrt(li_var_2022)
li_desv_2022
ls_var_2022=(27-1)*(desv_2022^2)/q1
ls_var_2022
ls_desv_2022=sqrt(ls_var_2022)
ls_desv_2022


#Letra C)----
#Diferença dos Dados
dados$dif <- dados$`Ano 2022`-dados$`Ano 2021`
media_dif=mean(dados$dif)
media_dif
desv_dif=sd(dados$dif)
desv_dif
n=length(dados$`Id Capital`)
n
t.test(dados$dif,mu=0,alternative=c("greater"),conf.level=0.95)
tc=qt(0.95,26)
tc
tobs=(media_dif-0)/(desv_dif/sqrt(27))
tobs
