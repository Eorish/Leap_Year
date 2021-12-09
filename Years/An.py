#Soma se o ano é bissexto, ou não é bissexto
def bissexto(ano): return ano % 4 == 0
ano = int(input('digite o ano : '))
if bissexto(ano ) :
    print('bissexto')
else:
    print('nao bissexto')
