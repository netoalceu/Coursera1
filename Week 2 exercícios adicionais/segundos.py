str_segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(str_segundos)%60
minutos =  int(str_segundos)//60
horas =  minutos//60
minutos =   minutos%60
dias = horas//24
horas =  horas%24

print("%d dias, %d horas, %d minutos e %d segundos." % (dias, horas, minutos, segundos))
