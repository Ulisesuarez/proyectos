"DOC"
PRECIOS = [1, 2, 3, 5, 9, 20, 30, 40, 80, 90, 100, 200, 300, 400]

def CalculadoDescuentos(precios):
    preci = list(precios) #hay que hacer una nueva lista!!!!
    for i in range(0, len(preci)):
        
        if preci[i] < 20:
            pass
        elif 20 < preci[i] <= 100:
            preci[i] = preci[i]-0.05*preci[i]
        elif preci[i] > 100:
            preci[i] = preci[i]-0.1*preci[i]
    return preci

Descuentos = CalculadoDescuentos(PRECIOS)
print("los precios rebajados son:")

for j in range (0, len(PRECIOS)):
    print("precio original "+str(PRECIOS[j])+ " precio descuento "+str(Descuentos[j]))
