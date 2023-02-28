inverter = ''
frase = str(input('Digite a palavra: '))
palavra = frase.split()
junto = ''.join(palavra)
inverter = ''

for letras in range(len(junto)-1, -1, -1):
	inverter = inverter + junto[letras]

print(inverter)
