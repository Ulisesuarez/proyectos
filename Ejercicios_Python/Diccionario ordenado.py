"Escribe     un programa que pida por teclado una cantidad de dinero y que a continuación muestre \
la descomposición de dicho importe en el menor número de billetes y monedas de 100, 50, 20, 10, 5, 2 \
y 1     euro. En el caso de que alguna moneda no intervenga en la descomposición no se tiene \
que visualizar nada en la pantalla. Para una cantidad de 2236 euros la salida \
generaría el programa sería"

import collections
print("Cuanto dinero quiere")
dineroinput = int(input())

def BilletesMinimos(dinero):
    
    bill_100=0
    bill_50=0
    bill_20=0
    bill_10=0
    bill_10=0
    bill_5=0
    mon_2=0
    mon_1=0
    dineroRestante=dinero
    if dineroRestante>=100:
        bill_100 = (dinero-dinero%100)/100
        dineroRestante = dinero%100
    if dineroRestante>=50:
        bill_50 = (dineroRestante-dineroRestante%50)/50
        dineroRestante= dineroRestante%50
    if dineroRestante>=20:
        bill_20 = (dineroRestante-dineroRestante%20)/20
        dineroRestante= dineroRestante%20
    if dineroRestante>=10:
        bill_10 = (dineroRestante-dineroRestante%10)/10
        dineroRestante= dineroRestante%10
    if dineroRestante>=5:
        bill_5 = (dineroRestante-dineroRestante%5)/5
        dineroRestante= dineroRestante%5
    if dineroRestante>=2:
        mon_2 = (dineroRestante-dineroRestante%2)/2
        dineroRestante= dineroRestante%2
    mon_1=dineroRestante

    return ({100:int(bill_100), 50:int(bill_50),20:int(bill_20), 10:int(bill_10), 5:int(bill_5),2:int(mon_2),1:int(mon_1)})


billetes = BilletesMinimos(dineroinput)

billOrden= collections.OrderedDict(sorted(billetes.items(), key=lambda t:t[0]))
for clave,valor in billOrden.items():
    if valor>0 and clave>2:
        print("%s billetes de %s" % (valor,clave))
    if valor>0 and clave<=2:
        print("%s monedas de %s" % (valor,clave))
    

        
        
        




        
