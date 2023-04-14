#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53


dic = {"SP":67836.43, "RJ":36678.66, "MG":29229.88, "ES":27165.48, "Outros":19849.53}

total = sum(dic.values())
print(total)

soma = 0;
for key in dic.keys():
    percent = (dic[key]*100)/total

    if(key == "Outros"):
        print("Os outros estados foram responsáveis por {:.2f}% do faturamento.".format(percent))
    else:
        print("O estado de {} representa {:.2f}% do faturamento mensal da distribuidora.".format(key, percent))

    soma+=percent

