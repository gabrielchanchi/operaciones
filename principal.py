import math

def calc_area(lado):
	area=lado*lado
	print(f"El area es {area}")
	
def calc_area_circulo(radio):
	area=math.pi*radio**2
	print(f"El área es {area}")
	
	
calc_area(2)
calc_area_circulo(3)
	
