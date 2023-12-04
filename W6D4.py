print("Ciao! Calcoliamo insieme il perimetro di alcune forme geometriche")
print("\nIniziamo con il quadrato!")
lato_quadrato = input("Inserisci la misura del lato:")
perimetro_quadrato = float(lato_quadrato) * 4
print("Il perimetro del quadrato e' " + str(perimetro_quadrato))

print("\nAndiamo avanti con il cerchio!")
raggio_cerchio = input("Inserisci la misura del raggio:")
circonferenza = 2 * 3.14 * float(raggio_cerchio)
print("La circonferenza del cerchio e' " + str(circonferenza))

print("\nE finiamo con il rettangolo!")
base = input("Inserisci la misura della base:")
altezza = input("Inserisci la misura dell'altezza:")
perimetro_rettangolo = float(base) * 2 + float(altezza) * 2
print("Il perimetro del rettangolo e' " + str(perimetro_rettangolo))

print("\nIl mio lavoro qui e' finito! Ciao!")
