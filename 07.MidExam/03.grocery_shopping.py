products = input().split("|")

while True:
    command = input()

    if command == "Shop!":
        break

    command_split = command.split("%")
    command_action = command_split[0]
    product = command_split[1] if len(command_split) > 1 else None

    if command_action == "Important":
        if product in products:
            products.remove(product)
        products.insert(0, product)

    elif command_action == "Add":
        if product in products:
            print("The product is already in the list.")
        else:
            products.append(product)

    elif command_action == "Swap":
        product1, product2 = command_split[1], command_split[2]
        if product1 in products and product2 in products:
            index1, index2 = products.index(product1), products.index(product2)
            products[index1], products[index2] = products[index2], products[index1]
        else:
            missing_product = product1 if product1 not in products else product2
            print(f"Product {missing_product} missing!")

    elif command_action == "Remove":
        if product in products:
            products.remove(product)
        else:
            print(f"Product {product} isn't in the list.")

    elif command_action == "Reversed":
        products.reverse()

for idx, product in enumerate(products, start=1):
    print(f"{idx}. {product}")
