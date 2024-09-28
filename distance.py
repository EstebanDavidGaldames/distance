print("Cálculo de distancia entre dos puntos.")
print("\n")
def distancia(point1 : tuple, point2 : tuple):
  return ((point2[1]-point1[1])**2+(point2[0]-point1[0])**2)**0.5
