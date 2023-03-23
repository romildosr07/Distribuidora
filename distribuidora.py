"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do
valor total mensal da distribuidora.
 """""

faturamento_regiao = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}
soma = 0

for key in faturamento_regiao:
    soma += faturamento_regiao[key]

faturamento_lista = []
for key in faturamento_regiao:
   aux = faturamento_regiao[key] * 100
   percent = aux/soma

   obj = {
       key: '{:.2f}%'.format(percent)
   }

   faturamento_lista.append(obj)

for i in range(len(faturamento_lista)):
    aux = faturamento_lista[i]
    print(aux)


