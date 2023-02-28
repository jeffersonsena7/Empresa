faturamento = {22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174,
			   11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0,
			   35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318,
			   1718.1221,13220.495, 8414.61}

sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953

media = 0
total = 0
mediamensal = 0

for f in faturamento:
	if f > 0:
		total = total + f
media = total / 21

percentualsp = (sp * 100) / total
percentualrj = (rj * 100) / total
percentualmg = (mg * 100) / total
percentuales = (es * 100) / total
percentualoutros = (outros * 100) / total
print('=-' *50)
print('')
for lista in faturamento:
		if lista < media:
			mediamensal += 1

print('--' *50)
print(f'O menor valor de faturamento ocorrido em um dia do mês: {min(faturamento)}')
print('--' *50)
print(f'O maior valor de faturamento ocorrido em um dia do mês: {max(faturamento)} ')
print('--' *50)
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi: {mediamensal} dias')
print('=-' *50)
print(f'O percentual de SP foi: {percentualsp} % do valor total mensal da distribuidora')
print('--' *50)
print(f'O percentual de RJ foi: {percentualrj} % do valor total mensal da distribuidora')
print('--' *50)
print(f'O percentual de MG foi: {percentualmg} % do valor total mensal da distribuidora')
print('--' *50)
print(f'O percentual de ES foi: {percentuales} % do valor total mensal da distribuidora')
print('--' *50)
print(f'O percentual de OUTROS foi: {percentualoutros} % do valor total mensal da distribuidora')
print('--' *50)
