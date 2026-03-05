# Floats VS Decimales
# Difieren principalmente en la precision
# los decimales son mas precisos y los float redondean los decimales


from decimal import Decimal

product_cost_float = 88.40
commission_rate = 0.08
qty = 450

product_cost_float += (commission_rate * product_cost_float)
print(product_cost_float * qty) # 42962.4

product_cost_decimal = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost_decimal += (commission_rate * product_cost_decimal)
print(product_cost_decimal * qty) # 42962.40000000000282883716451


#Podemos convertir las varibles a otros tipos de datos pon 

print(int(product_cost_float))
print(float(qty))
print(Decimal(product_cost_float))
print(complex(commission_rate))


