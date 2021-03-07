# Sal's Shipping execrcise -> Codecademy - Learn Python 3

weight = 8.4

# ground shipping
gs_flat_charge = 20
if weight <= 2:
  print(1.5 * weight + gs_flat_charge)
elif weight > 2 and weight <= 6:
  print(3.0 * weight + gs_flat_charge)
elif weight > 6 and weight <= 10:
  print(4.0 * weight + gs_flat_charge)
elif weight > 10:
  print(4.75 * weight + gs_flat_charge)

# premium ground shipping
pgs_flat_charge = 125
print(pgs_flat_charge)

# drone shipping
if weight <= 2:
  print(4.5 * weight)
elif weight > 2 and weight <= 6:
  print(9.0 * weight)
elif weight > 6 and weight <= 10:
  print(12.0 * weight)
elif weight > 10:
  print(14.00 * weight)
