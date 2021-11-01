sgtotal = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = sgtotal // 86400
sgrest1 = sgtotal % 86400
horas = sgrest1 // 3600
sgrest2 = sgrest1 % 3600
minutos = sgrest2 // 60
segundos = sgrest2 % 60
print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')


