dinheiro_hora = float(input("Insira quanto você ganha por hora, utilize o ponto para decimal: "))
horas_mes = float(input("Insira quantas horas você trabalha por mês, utilize o ponto para decimal: "))
salario_bruto = dinheiro_hora * horas_mes
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto *  0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato
print ("Salário Bruto: R$", salario_bruto, "\nIR(11%): R$", imposto_de_renda, "\nINSS(8%): R$", inss, "\nSindicato(5%): R$", sindicato, "\nLíquido: R$", salario_liquido)
