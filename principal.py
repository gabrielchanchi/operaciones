import math

def calc_area(lado):
	area=lado*lado
	print(f"El area es {area}")
	
def calc_area_circulo(radio):
	area=math.pi*radio**2
	print(f"El área es {area}")

def calcular_perimetro(radio):
	perim=2*math.pi*radio
	print(f"El perímetro es {perim}")
	
calc_area(2)
calc_area_circulo(3)
calcular_perimetro(4)	
