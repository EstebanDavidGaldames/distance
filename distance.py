print("Cálculo de distancia entre dos puntos.")
print("\n")
def distancia(point1 : tuple, point2 : tuple):
  return ((point2[1]-point1[1])**2+(point2[0]-point1[0])**2)**0.5

punto1 = (float(input("Ingrese la cordenada x del primer punto: ")), float(input("Ingrese la cordenada y del primer punto: ")))
print(f'Punto 1 = {punto1}')
punto2 = (float(input("Ingrese la cordenada x del segundo punto: ")), float(input("Ingrese la cordenada y del segundo punto: ")))
print(f'Punto 2 = {punto2}')
distance = distancia(punto1, punto2)
print(f'La distancia entre los puntos es {distance}.')
