sandwich_orders = ["atum", "frango", "vegetariano", "presunto e queijo"]
finished_sandwiches = []

for pedido in sandwich_orders:
    print("Preparando seu sanduíche de " + pedido + ".")
    finished_sandwiches.append(pedido)

print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print("- " + sanduiche)
