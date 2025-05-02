import pandas as pd

df=pd.read_csv("Tabela-Dados.csv")

df['sexo']=df['sexo'].replace({
    "Masculino" : "Masculino",
    "M" : "Masculino",
    "masc" : "Masculino",
    "Feminino" : "Feminino",
    "F" : "Feminino",
    "fem" : "Feminino",
})
#aqui eu estou trocando as virgulas por ponto para que consiga transformar em float
df[["nota_matematica", "nota_portugues"]] = df[["nota_matematica", "nota_portugues"]].applymap(lambda x: str(x).replace(",","."))

#aqui estou transformando todas as notas em foat para conseguir fazer os calculos, pois vi que não conseguiria se estivessem com ','
df[["nota_matematica", "nota_portugues"]] = df[["nota_matematica", "nota_portugues"]].astype(float)

#aqui estou criando a média solicitada, colocando limite de dois decimais para que fique mais limpo de ser visualizado
df["Media"]=((df["nota_matematica"]+df["nota_portugues"]+(df["frequencia"]/10))/3).round(2)

#aqui estou criando a coluna aprovado
df["aprovado"]=df["Media"]>=7

#aqui estou definindo aprovado como string ao invés de booleano
df["aprovado"]=df["aprovado"].astype(str)

#aqui estou definindo que apareça Sim e Não ao invés de True ou False para afirmativas e negativas, como foi solicitado
df["aprovado"]=df["aprovado"].replace({
    "True" : "Sim",
    "False" : "Não"
})
#Aqui estou trocando todos os . por virgula, linha a linha usando applymap assim como fiz anteriormente para trocar todas as virgulas pra ponto

df[['nota_matematica', 'nota_portugues','frequencia','Media']] = df[['nota_matematica', 'nota_portugues','frequencia','Media']].applymap(lambda x: str(x).replace(".",","))


print(df)

df.to_csv("Tabela-Saida.csv") 