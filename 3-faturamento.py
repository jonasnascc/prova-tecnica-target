import json

with open('dados.json') as data:
    dados = json.load(data)


maior_valor = 0
menor_valor = 0


sum = 0;
for i in range(len(dados)):
    d = dados[i]
            
    if(i==0):
        maior_valor = d['valor']
        menor_valor = d['valor']
    elif(d['valor'] > 0):
            menor_valor = min(d['valor'], menor_valor)
            maior_valor = max(d['valor'], maior_valor)

    sum+=d['valor']

media = sum/30

n = 0
for i in range(len(dados)):
    d = dados[i]
    if(d['valor'] > media):
        n+=1
        
print("O MENOR valor de faturamento ocorrido em um dia do mês foi de: {}".format(menor_valor))
print("O MAIOR valor de faturamento ocorrido em um dia do mês foi de: {}".format(maior_valor))

print("O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi: {}".format(n))


    
